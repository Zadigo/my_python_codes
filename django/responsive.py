import re

class Mobiles:
    def __init__(self, name=None):
        self.name = name
        self.mobiles = {
            'samsung': {
                's5': { 'height': 640, 'width': 360 },
                's9': { 'height': 812, 'width': 374 },
                's9 plus': { 'height': 740, 'width': 360 }
            },
            'iphone': {
                '5': { 'height': 568, 'width': 320 },
                '6': { 'height': 667, 'width': 375 },
                '6s': { 'height': 667, 'width': 375 },
                '6 plus': { 'height': 736, 'width': 414 },
                '6s plus': { 'height': 736, 'width': 414 },
                '7': { 'height': 667, 'width': 375 },
                '7 plus': { 'height': 736, 'width': 414 },
                '8': { 'height': 667, 'width': 375 },
                '8 plus': { 'height': 736, 'width': 414 },
                'x': { 'height': 812, 'width': 375 },
                'xr': { 'height': 896, 'width': 414 },
                'xs': { 'height': 812, 'width': 375 },
                'xs max': { 'height': 896, 'width': 414 }
            }
        }

    def __repr__(self):
        return self.__unicode__()

    def __unicode__(self):
        if self.name:
            return str(self.mobiles[self.name])
        return str(self.mobiles)

    def __getitem__(self, name):
        return self.mobiles[name]

print(Mobiles(name='samsung'))

class Responsive:
    """A class that detects if a request comes from a mobile
    or not by testing the User-Agent of the request.

    Description
    -----------

        Returns True or False if a mobile or not
    """
    def __init__(self, request):
        # Process the user agent from
        # the request
        self.user_agent = request.META.get('HTTP_USER_AGENT')
        
        # Detect if mobile is in the header --
        # General test to check if mobile
        pattern = r'([m|M]obile)'
        is_match = re.search(pattern, self.user_agent)
        if is_match:
            mobile = True
        else:
            mobile = False

        # Additional test. Detect if iPhone
        # or Android. Confirms for sure then
        # that it is indeed a mobile phone
        pattern = r'(i[p|P]hone|Android)'
        is_match = re.search(pattern, self.user_agent)
        if is_match:
            self.mobile_type = is_match.group(1)
            confirmation_test = True
        else:
            confirmation_test = False

        # Now we know if we're dealing with a
        # mobile phone or not
        self.mobile = bool(mobile and confirmation_test)
