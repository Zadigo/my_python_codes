import re

# Az@text.fr
# a.z@text.fr
# a.z-b@text.fr
# a.z@etu.univ-lille3.fr
PATTERNS = [
    r'([a-zA-Z]+(\.|\_|\-)[a-zA-Z]+)\@\w+\.\w+',
    r'([a-zA-Z]+\@\w+\.\w+)',
    r'([a-zA-Z]+\.[a-zA-Z]+\-[a-zA-Z]+)\@\w+\.\w+',
    r'(\w+\.\w+)\@(etu\.univ\-(lille)\d{1}\.fr)'
]

class EmailAnalyzer(object):
    """
    This module is used to analyze email adresses
    in order to determine the ones that are viable.

    It appends each mail listed as correct into a
    `email_list` container that can be be iterated
    on for additional purposes.

    Update the `PATTERNS` list for for REGEX in
    order to check for a particular email adress.

    It inclucdes patterns such as :
    >> yourmail@something.com
    >> your.mail@something.com
    >> your-mail@something.com
    >> your_mail@something.com
    >> your.mail-other@something.com
    >> your.mail@etu-univ.lille{1,2...}.fr
    """
    email = None

    def __init__(self, request=None, *args, **kwargs):
        if request:
            if request.method == 'POST':
                if self.email == None:
                    self.email = request.POST['email']

    def analyze(self):
        email_list = []

        for PATTERN in PATTERNS:
            result = re.search(PATTERN, self.email)

            if result is not None:
                if self.email == result.group(0):
                    email_list.append(result.group(0))
                
                return email_list