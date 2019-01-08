import string
import random
import datetime
from hashlib import sha256
from urllib.parse import urlencode

ALLOWED_CHARS = string.digits + string.ascii_lowercase + string.ascii_uppercase

def create_random_token(length=15):
    return ''.join(random.choice(ALLOWED_CHARS) for i in range(length))


def create_salt_token(length=15):
    token_one = ''.join(random.choice(ALLOWED_CHARS) for i in range(length))
    token_two = ''.join(random.choice(ALLOWED_CHARS) for i in range(length))
    indexes = zip((token_one.index(x) for x in token_one), (token_two.index(x) for x in token_two))
    cipher = ''.join(ALLOWED_CHARS[(x + y) % len(ALLOWED_CHARS)] for x, y in indexes)
    return token_one + cipher


def date_helper(method=[]):
    """
    Get the current date with an empty method.

    Add or substract days to a given date by sending
    an liste `[addition, 1999-01-01, days_to_add]` or
    `[substract, 1999-01-01, days_to_substract]`.
    """
    def _method_checker():
        if len(method) != 3:
            raise KeyError('The method should have three components: [addition, 1999-01-01, days_to_add]')

    if not method:
        return datetime.datetime.now()

    else:
        _method_checker()

        date_string = method[1]

        if 'addition' in method:
            days_to_add = method[2]

            provided_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            new_date = provided_date + datetime.timedelta(days=days_to_add)

        if 'substraction' in method:
            days_to_substract = method[2]

            provided_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
            new_date = provided_date - datetime.timedelta(days=days_to_substract)

        return new_date


def get_time_stamp(time_string=''):
    if not time_string:
        return datetime.datetime.timestamp(datetime.datetime.now())

    user_time = datetime.datetime.strptime(time_string, '%Y-%m-%d')
    return datetime.datetime.timestamp(user_time)


def image_upload_helper(filename):
    """
    Uploads the file under a specific format in
    the /media/ folder.
    
    For instance if the file
    was uploaded under post 27, then it will
    appear as /27/filename/ as opposed to just
    /filename/.
    """
    return '%s/%s' % (random.randrange(1, 1000), filename)


def campaign_builder(url, utm_source, utm_medium, **kwargs):
    """
    Use  `utm_source` to identify a search engine, 
    newsletter name, or other source e.g google, twitter,
    newsletter

    Use `utm_medium` to identify a medium such as 
    email, referral, sms, cpc, organic, social

    Used for keyword analysis:
    Use `utm_campaign` to identify 
    a specific product promotion or strategic campaign.
    e.g. utm_campaign=spring_sale

    Use `utm_term` to note 
    the keywords for this ad e.g running+shoes

    Use `utm_content` to differentiate ads or links 
    that point to the same URL.

    Example:
    /?utm_campaign=theverge&utm_content=The+verge+article
    &utm_medium=social&utm_source=twitter&via=Verge
    """
    terms = {'utm_source':utm_source, 'utm_medium':utm_medium}
    if kwargs:
        for key, term in kwargs.items():
            terms.update({key: term})
    query = urlencode(terms)
    return url + '?' + query


class LinkShareGenerator:
    """
    Generate share links for the posts
    created for the blog.

    You can create Twitter and Facebook
    shareable links. 

    """
    absolute_uri = 'http://127.0.0.1:8000/blog/'
    url_facebook = 'https://www.facebook.com/sharer/sharer.php?'
    url_twitter = 'https://twitter.com/intent/tweet?'

    def __init__(self, post_title, request=None):
        self.post_title = post_title
        self.complete_url = urljoin(self.absolute_uri, post_title)

    @property
    def facebook(self):
        query = urlencode({
            'text':self.post_title,
            'u':self.complete_url,
        })
        return self.url_facebook + query

    @property
    def twitter(self):
        query = urlencode({
            'text':self.post_title,
            'url':self.complete_url,
        })
        return self.url_twitter + query