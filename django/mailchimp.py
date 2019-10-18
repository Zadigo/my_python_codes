import datetime
import secrets
from collections import namedtuple
from urllib.parse import urljoin

from requests.auth import AuthBase
from requests.sessions import Request, Session


class QuerySet:
    def __init__(self, category, obj:dict):
        cache = obj.copy()

        # Take out the out _links element
        # .. [{..., _links}, _links]
        cache.pop('_links')

        if category == 'lists':
            # Take out the item's _list elements
            # .. [{..., _links}]
            self.items = self.pop_links(cache['lists'])
            # Append the length element to the class
            self.length = cache['total_items']

        elif category == 'stores':
            pass

        # Create direct attributes so that we can
        # call the objects directly such as w.my_list
        self.create_attributes()

    def names(self):
        """Get all your lists' names
        """
        return self.query_values('name')

    def ids(self):
        return self.query_values('id')

    @staticmethod
    def pop_links(items:dict):
        values = []
        for item in items:
            item.pop('_links')
            values.append(item)
        return values

    def query_values(self, key):
        """A helper that queries the values from the
        Mailchimp JSON response
        """
        values = []
        for item in self.items:
            for name, value in item.items():
                if name == key:
                    values.append(value)
        return values

    def create_attributes(self):
        for item in self.items:
            name = item['name'].lower().replace(' ', '_')
            setattr(self, name, item)

class ApiKey(AuthBase):
    """Creates a header dict with authentication field for
    authorizing connections with API key
    """
    def __init__(self, key):
        self.key = key

    def __call__(self, h):
        h.headers['Authorization'] = f'auth {self.key}'
        return h

class MailChimp:
    """A class that helps interact with the Mailchimp API

    Parameters
    ----------
        
        datacenter: for example us14, us15...

        api_key: your api key on Mailchimp

        **headers: additional headers to add to the request
    """
    def __init__(self, datacenter, api_key, **headers):
        # Base path to access the API
        self.api = f'https://{datacenter}.api.mailchimp.com/3.0/'
        # Create the session that will be used
        # to send a prepared request
        self.session = Session()
        # Create the headers that will be used
        # in relationship wit the request
        self.headers = {
            'Authorization': f'auth {api_key}',
            'Cache-Control': 'no-cache'
        }
        self.api_key = ApiKey(api_key)

        if headers:
            # Update the headers if necessary
            self.headers = {**self.headers, **headers}

    def get(self, path):
        """Base definition that will be used to send all GET requests
        to the Mailchimp API

        Parameters
        ----------

            path: is the path to append to the base API url
        """
        request = Request('GET', self.build_url(path), auth=self.api_key)
        prepared_request = self.session.prepare_request(request)

        try:
            response = self.session.send(prepared_request)
        except:
            raise
        else:
            if response.status_code == 200:
                return response.json()
            return None

    def post(self, path, data:dict):
        """Base definition that will be used to send all POST requests
        to the Mailchimp API

        Parameters
        ----------

            path: is the path to append to the base API url
        """
        # For whatever reason, the API returns an error
        # if 'merged_fields' is not present in the request
        # body -- if not present, we need to implement it
        if 'merge_fields' not in data:
            data.update({'merge_fields': {}})

        request = Request('POST', self.build_url(path), headers=self.headers, json=data)
        prepared_request = self.session.prepare_request(request)

        try:
            response = self.session.send(prepared_request)
        except:
            raise
        else:
            print(response.text)
            if response.status_code == 200:
                return response.json()
            return None

    def build_url(self, path):
        return urljoin(self.api, path)

    def create_key(self, n=10):
        return secrets.token_hex(n)

class Lists(MailChimp):
    def _all(self):
        """Get all your lists
        """
        # return self.get('lists')
        return QuerySet('lists', self.get('lists'))

    def retrieve(self, id):
        """Get a specific list

        Parameters
        ----------
            id: for example 9wt02a1368
        """
        return self.get('lists/%s' % id)

    def create(self, name, contact:dict, permission_reminder, 
                campaign_defaults:dict, email_type_option=False):
        """
        Create a new list

        Parameters
        ----------

            name: refers to the name of the list

            contact: contact information displayed in campaign footers 
            to comply with international spam laws.

                {
                    company: '',
                    address1: ''
                    address2: '',
                    city: '',
                    state: '',
                    zip: '',
                    country: FR, US...,
                    phone: ''
                }

            permission_reminder: a text that makes it clear where your recipients 
            signed up for your email marketing

            campaign_defaults: default values for campaigns created for this list.

                {
                    from_name: CompanyA
                    from_email: companya@gmail.com,
                    subject: We are here!
                    language: french
                }

            email_type_option: whether the list supports multiple formats for emails. When set
            to True, the user can decide between HTML or plain text emails, otherwise, it becomes
            html by default with plain text as back up
        """
        data = {
            'name': name,
            'contact': contact,
            'permission_reminder': permission_reminder,
            'campaign_defaults': campaign_defaults,
            'email_type_option': email_type_option
        }
        return self.post('lists', data)

class Stores(MailChimp):
    """This class is specific to an ecommerce stores on Mailchimp. They allow for ecommerce platforms
    to create a store that can trigger a different amount of functionalities in relation their
    orders, habits...
    """
    def _all(self):
        """Get ecommerce stores
        """
        return self.get('ecommerce/stores')

    def retrieve(self, id):
        """Get a specific store

        Parameters
        ----------
            id: for example 9wt02a1368
        """
        return self.get('ecommerce/stores/%s' % id)

    def create(self, list_id, name, domain, email_address):
        data = {
            'id': self.create_key(),
            'list_id': list_id,
            'name': name,
            'domain': domain,
            'email_address': email_address,
            'currency_code': 'EUR',
            'money_format': '€',
            'primary_locale': 'fr',
            'phone': '0668552975',
            'address': {
                'city': 'Lille',
                'country': 'France'
            }
        }
        print(data)
        return self.post('ecommerce/stores', data)

    def new_customer(self, store_id, email_address, first_name, 
            last_name, orders_count, total_spent, opt_in_status=False, **kwargs):
        """Create a new customer in the store
        """
        data = {
            'id': self.create_key(),
            'email_address': email_address,
            'first_name': first_name,
            'last_name': last_name,
            'orders_count': orders_count,
            'total_spent': total_spent,
            'opt_in_status': opt_in_status,
            'address': {
                'address1': '',
                'address2': '',
                'city': '',
                'postal_code': '',
                'country': '',
                'country_code': ''
            }
        }
        return self.post(f'ecommerce/stores/{store_id}/customers', data)

    def new_order(self, order_id, store_id, customer, order_total, 
                    discount_total, shipping_total, lines:list, **kwargs):
        """Create a new order in the store

        Description
        -----------

            Once the customer has finalized his purchase, call this function to create
            a new order in Mailchimp which will create Order notifications in return.

            They consists of mails that sent to the customer related to the status of
            his order. They are triggered but the ``finaancial_status`` field in the data.

            Note that if the customer does not exist in the store, he will be automatically
            created upon calling this definition.

        Parameters
        ----------

            financial_status: paid, pending, refunded, cancelled, shipped

            lines: products sold

                [
                    {
                        id: A unique identifier for the order line item,
                        product_id: 
                        quantity:
                        price:
                        discount:
                    }
                ]
        """
        data = {
            'id': order_id,
            'customer': {
                'id': '64e8396cda3a9b5e50fd',
                'email_address': 'pendenquejohn@gmail.com',
                'opt_in_status': False
            },
            'currency_code': 'EUR',
            'orders_count': order_total,
            'discount_total': None,
            'shipping_total': shipping_total,
            'processed_at_foreign': str(datetime.datetime.now()),
            'shipping_address': {
                'name': '',
                'address1': '',
                'address2': '',
                'city': '',
                'postal_code': '',
                'country': '',
                'country_code': ''
            },
            'financial_status': 'pending',
            'lines': []
        }
        return self.post(f'ecommerce/stores/{store_id}/customers', data)

class Products(MailChimp):
    pass

order_id = 'zlkenfzoienfozienfoz'
list_id = '3335ddb952'
customer_id = '64e8396cda3a9b5e50fd'
store_id = '3b0c488c2c05b569914e'

stores = Stores('us15', '03351c2235cfe08e38995805b658311c-us15')
result = stores.new_order(
    order_id,
    store_id,
    {},
    175,
    0,
    0,
    [
        {
           'id': 'srknfosino',
           'produt_id': 'zionfzoeinf',
            'quantity': 15,
            'price': 415,
            'discount': 0 
        }
    ]
)
print(result)