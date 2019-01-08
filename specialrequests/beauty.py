import collections

try:
    from bs4 import BeautifulSoup
except ImportError as e:
    print("Beautiful is not installed. \
        Use 'pip install bs4'")

# from sr_responses.response import BaseResponse


class BeautifulResponse:
    responses = Responses()._response_engine

    def __init__(self, *args, **kwargs):
        if callable(responses):
            if isinstance(responses, BaseResponse):
                pass
            else:
                pass
        else:
            if isinstance(responses, (list, tuple)):
                pass

        self.responses = responses

    @staticmethod
    def _soup_factory(response_object):
        """
        Parses the HTML text for each response
        """
        return BeautifulSoup(response_object.text, 'html.parser')

    def html_tags(self):
        tags = [tag for tag in self._soup_factory(self.responses)]
        return tags

class ExtractImages(BeautifulResponse):
    def get_images(self):
        tags = super().html_tags()
        return tags.findall('img')

class ExtractLinks(BeautifulResponse):
    pass

class ExtractEmails(BeautifulResponse):
    pass

class ExtractTable(BeautifulResponse):
    pass

# BEAUTY = collections.namedtuple('HTML', ['text'])

# class BeautifulResponse(BaseResponse):
#     response = None
#     html_tags = None
#     # instance = BaseResponse()

#     @staticmethod
#     def _soup_factory(html_tags):
#         return BeautifulSoup(html_tags.text, 'html.parser')

#     # def beautify_response(self, Klass=None):
#     #     # We have to be able to get an instance
#     #     # wether we call method from class
#     #     # or if we superclass
#     #     if  Klass is None:
#     #         Klass = self.instance

#     #     # If instance is a method
#     #     if not isinstance(Klass, BaseResponse):
#     #         is_callable = callable(Klass)
#     #         if is_callable:
#     #             # We have to pass response in a list
#     #             # for now otherwise we get a byte response
#     #             # since Beautiful soup is looking for a list
#     #             # to iterate over
#     #             self.response = [Klass()]
                
#     #             if self.response:
#     #                 pass
#     #             else:
#     #                 raise TypeError('Response is None.')

#     #         else:
#     #             raise TypeError('You should pass a function or an instance. Received %s' % Klass)

#     #     else:
#     #         # We need to set attributes of the
#     #         # empty instance method otherwise
#     #         # they would be none
#     #         Klass.__setattr__('urls', self.urls)
#     #         Klass.__setattr__('useragent', self.useragent)
#     #         self.response = Klass.get_response()

#     #     if self.response:
#     #         # Keep only responses that received a
#     #         # status_code of 200
#     #         sorted_response = [response for response in self.response if response.status_code == 200]
            
#     #         if len(sorted_response) == 0:
#     #             return []
#     #     else:
#     #         return []

#     #     # Get the html text elements from
#     #     # each response and return a list
#     #     self.html_tags = [self._soup_factory(single_response) for single_response in sorted_response]

#     def beautify_response2(self):
#         self.response = super(BeautifulResponse, self).raw_response()
#         self.html_tags = [self._soup_factory(resp) for resp in self.response]
#         return self.html_tags

# class ExtractImages(BeautifulResponse):
#     """
#     This extracts all images from the html tags
#     """
#     def get_images(self):
#         super(ExtractImages, self).beautify_response2()
#         return self.html_tags[0].findAll('img')

# class A(ExtractImages):
#     url='http://www.sawfirst.com'

# print(A().get_images())

# class ExtractLinks(BeautifulResponse):
#     """
#     This extracts all images from the html tags
#     """
#     def get_links(self):
#         super().beautify_response()
#         return self.html_tags[0].findAll('a')

# class ExtractTable(BeautifulResponse):
#     """
#     This extracts all images from the html tags
#     """
#     def get_links(self, **kwargs):
#         super().beautify_response()
#         if 'class_name' in kwargs:
#             return self.html_tags[0].find('table', _class=kwargs['class_name'])