# https://stripe.com/docs/api/python#capture_charge

import stripe

STRIPE_TOKEN = 'sk_test_QkRv7ivfBRfQZiYzIfsOTd68'
stripe.api_key = STRIPE_TOKEN

def create_charge(amount, customer, description=None, receipt_email=None, **kwargs):
    # # Generate order_id
    # if not 'order_id' in kwargs:
    #     kwargs['order_id']=6735
    # if customer:
    #     kwargs['customer'] = customer
    charge = stripe.Charge.create(
        amount=2000,
        currency="eur",
        # source="tok_amex",
        customer=customer,
        description=description,
        receipt_email=receipt_email,
    )
    return charge['id']

def retrieve_charge(charge_id, **kwargs):
    return stripe.Charge.retrieve(charge_id)

def retrieve_customer(customer_id):
    """
    Retrieve a customer from stripe by
    passing a customer ID using the
    following format : cus_D77bepa8CiNlFB
    """
    return stripe.Customer.retrieve(customer_id)

# def create_customer(request='', description, email=None, source='tok_visa'):
#     """
#     Create a customer in new customer in Stripe.
#     Returns a customer ID.

#     """
#     # user_id = request.user.id
#     # cust_id_exists = Model.objects.get(id=user_id).stripe_id
#     # if cust_id_exists:
#     #     raise stripe.error.StripeError(message='The customer exits in the database')

#     customer = stripe.Customer.create(
#         email=email,
#         description=description,
#         source=source
#     )
#     return customer['id']

def create_bank_account(customer_id='', source=''):
    customer = stripe.Customer.retrieve("cus_DDwI2EG2PemOE4")
    customer.sources.create(source="btok_1CnVz92eZvKYlo2Cmwchuqte")

print(create_bank_account())
