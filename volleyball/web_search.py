from googlesearch.googlesearch import GoogleSearch


class WebSearch:
    def __init__(self, q):
        result = list(GoogleSearch().search(q, num_results=5))
        print(result)

WebSearch('Ekaterina Efimova')