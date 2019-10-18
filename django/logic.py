"""A module that logics the payment process with Stripe for a
Django website
"""

try:
    import stripe
    from mailchimp import Stores
except ImportError:
    pass
else:
    stores = Stores('us15', '')
import os
import re

from django.http.response import JsonResponse

from accounts.models import MyAnonymousUser
from shop.models import AnonymousCart
from shop.utilities import create_reference

# Use production key in production
# and development key on DEBUG sessions
# e.g. sk_live_ or sk_test_
if os.environ.get('DEBUG') == 'True':
    stripe.api_key = ''
else:
    stripe.api_key = ''

class StripeCharge:
    """Takes the charge response and objectifies it
    in order to add functionnalities or allow better
    further processes on the dict.
    """
    def __init__(self, charge: dict):
        self.charge = charge
    
    @property
    def _id(self):
        """
        Description
        -----------

            billing_details: {
                address: {
                    city: None,
                    country: None,
                    line1: None,
                    line2: None,
                    postal_code: None,
                    state: None
                },
                "email": jennyrosen@email.com,
                "name": "Jenny Rosen",
                "phone": null
            }
        """
        return self.charge['id']

    @property
    def amount(self):
        return self.charge['amount']
    @property
    def billing_details(self):
        return self.charge['billing_details']

    @property
    def status(self):
        return self.charge['status']

class ProcessPayment:
    """A class that helps simplify the payment process
    with Stripe.
    """
    def __init__(self, request, stripe_token, user_infos: dict):
        self.base_response = {
            'status': None,
            'redirect_url': None
        }

        self.stripe_token = stripe_token

        # Check that the user information have all the
        # required fields in order to prevent KeyError
        # below when referencing to these fields
        self.user_infos = self.check_user_infos(user_infos)

        self.request = request

        # Create a reference for the
        # order here
        self.order_reference = create_reference()

        self.total_of_products_to_buy = 0

        # This parameter returns an charge
        # object that can be used for other
        # kinds of processing afterwards
        self.completed_charge = None

        # Access the user once the payment
        # process has been done
        self.anonymous_user = None

    def payment_processor(self, model:type=None, fields:dict=None, **kwargs):
        """Process a payment and get the charge as an object
        for further processing.

        Description
        -----------

            StripeCharge(charge)

        Parameters
        ----------

            model: pass a database model if you wish to process the
                   the user in your database

            **fields: represent the fields that you wish to use when
                      creating the user in the database
        """
        total_of_products_to_buy = 0

        # Get the cart iD from the session 
        # and if it is none, then return 0
        # because the user has nothing to
        # pay for
        try:
            cart_id = self.request.session['cart_id']
        except KeyError:
            self.base_response.update(
                {
                    'status': 500,
                    'redirect_url': '/shop/cart/',
                    'order_reference': None,
                    'reason': 'No cart iD'
                }
            )
            return self.response()
        else:
            # Products in the cart
            products = AnonymousCart.anonymous_manager.related_products(cart_id)
            # Total of the cart
            total_of_products_to_buy = AnonymousCart.anonymous_manager.cart_sum(cart_id)

        if total_of_products_to_buy != 0:
            amount = self.price_to_stripe(total_of_products_to_buy)
            # Now we can create the dict that will be used
            # to process the payment -- In this case, we do
            # need the customer_id for now since we are not
            # registering customers to charge.
            # We just need their card.
            params = {
                # 'customer': customer_id,
                'amount': amount,
                'currency': 'eur',
                'source': self.stripe_token,
                'description': 'This is an order for cart %s' % cart_id,
                'receipt_email': self.user_infos['email'],
                'shipping': {
                    'address': {
                        'line1': self.user_infos['address'],
                        'city': self.user_infos['city'],
                        'postal_code': self.user_infos['zip_code']
                    },
                    'name': 'Clothes',
                    'phone': self.user_infos['telephone']
                    # 'tracking_number': '4ZR3234FZ'
                    # 'carrier': self.user_infos['shipping'],
                },
                'metadata': {
                    'order_reference': self.order_reference,
                    'shipping': self.user_infos['shipping']
                }
            }
            # There we create the charge
            charge = stripe.Charge.create(**params)
            
            if charge['status'] == 'succeeded':
                # If the payment was successful,
                # then we can redirect the user
                # to the success page
                url = '/shop/cart/success-page/?order=' + self.order_reference.lower()

                # We can mark the products as paid
                # for so that we can proceed to sending
                # them the customer

                # And then create and anonymous customer
                # so that we can keep track from our
                # admin interface
                # self.anonymous_user = self.create_anonymous_user('', fields)
                self.anonymous_user = self.create_anonymous_user(cart_id)
                # Now associate the products to the user
                products.update(user=self.anonymous_user)

                # Now we can create the order in our
                # database for each product that was
                # paid for by the customer

                # We can also process the new order and customer
                # with Mailchimp's API
                # try:
                #     from mailchimp import Stores
                # except:
                #     pass
                # else:
                #     stores = Stores('', '')
                #     customer = {
                #         'id': '',
                #         'email_address': self.anonymous_user.email
                #     }
                #     new_order = stores.new_order(self.order_reference, '', 
                #                             customer, amount, 0, amount, [])

                # Now this the response that will be returned
                # to the AJAX function that called to process
                self.base_response.update(
                    {
                        'status': 200,
                        'redirect_url': url,
                        'order_reference': self.order_reference
                    }
                )

        else:
            # Just return some sort of
            # error response
            self.base_response.update(
                {
                    'status': 500,
                    'redirect_url': '/shop/cart/',
                    'order_reference': self.order_reference
                }
            )

        return StripeCharge(charge)

    def response(self):
        """Get a valid response for Django view in relation
        to the payment
        """
        status = self.base_response['status']
        return JsonResponse(self.base_response, safe=False, status=status, content_type='json')

    def create_anonymous_user(self, cart_id, model:type=None, **fields):
        """Create an anonymous user in our database for marketing and remarketing
        reasons. This also serves as way to keep a link between what was ordered
        by which customer with his related details.
        """
        # user = model.objects.create(**fields)
        user = MyAnonymousUser.objects.create(cart=cart_id, email=self.user_infos['email'],
                        address=self.user_infos['address'], zip_code=self.user_infos['zip_code'])
        return user

    def cleaned_data(self, email, telephone):
        email = re.match(r'^\w+(?:\.|\-\_)?\w+\@\w+\.\w+$', email)
        telephone = re.match(r'^(\+\d{1,2})?(\d{10})$', telephone)


    @staticmethod
    def price_to_stripe(price):
        # Stripe does not take decimals so we have to
        # multiply by a hundred to fit the dict
        # E.g. 12.95€ is 1295 in Stripe format
        return int(price * 100)

    @staticmethod
    def check_user_infos(user_infos: dict):
        """Checks whether some parameters are present in the
        dictionnary that was passed. If not, proceeds to update
        that dictionnary with the missing values marked as None

        Description
        -----------

            A base dictionary should have the following pieces
            of information:

            {
                email: 
                address:
                city:
                zip_code:
                shipping:
            }
        """
        if 'email' not in user_infos:
            user_infos.update({'email': None})

        if 'telephone' not in user_infos:
            user_infos.update({'telephone': 000000})

        if 'address' not in user_infos:
            user_infos.update({'address': None})

        if 'city' not in user_infos:
            user_infos.update({'city': None})

        if 'zip_code' not in user_infos:
            user_infos.update({'zip_code': None})

        if 'shipping' not in user_infos:
            user_infos.update({'shipping': None})

        return user_infos
