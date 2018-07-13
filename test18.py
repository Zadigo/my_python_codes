import re

BAD_WORDS  = [
    'bitch',
    'bish'
]

PATTERNS = ['(' + BAD_WORD + ')([a-zA-Z0-9_]+)' for BAD_WORD in BAD_WORDS]

class TextAlgorithm:
    def __init__(self, text):
        self.new_text = ''
        if text:
            self.text = text
            if isinstance(text, str):
                self.words = self.parse_text()
            else:
                pass
        else:
            pass
    
    def parse_text(self):
        words = self.text.split(' ')
        return words
    
    def test_words(self):
        # new_text = ' '
        for word in self.words:
            if word in BAD_WORDS:
                self.new_text += '*****' + ' '
            else:
                self.new_text += word + ' '

    def deep_find(self):
        self.test_words()
        for PATTERN in PATTERNS:
            regex_search = re.search(PATTERN, self.new_text)
            if regex_search:
                print(regex_search.groups())
                newer_text = self.new_text.replace(regex_search.group(0), '*****')
                return newer_text
            else:
                return self.new_text

print(TextAlgorithm('This is a bitchplease bishtext. This is why this bitch is not in tennis.').deep_find())