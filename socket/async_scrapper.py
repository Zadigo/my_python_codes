import argparse
import asyncio
import queue
import threading
from collections import OrderedDict, deque
from concurrent.futures import ThreadPoolExecutor
import time
import requests
from bs4 import BeautifulSoup

# results = OrderedDict()

# async def algorithm(soup):
#     pass

# async def create_soup(responses):
#     htmls = deque()
#     for response in responses:
#         if response:
#             htmls.append(BeautifulSoup(response.text, 'html.parser'))
#     return htmls

# async def main_soup():
#     values = await create_soup(results)
#     return values

# def response_handler(url, index):
#     """Checks and stores the response appropriately"""
#     print(f'[GET] Fetching: {url}')
#     response = requests.get(url)
#     results[index] = response if response.status_code == 200 else None
#     return results

# def prepare_urls(func):
#     urls_queue = Queue(maxsize=0)
#     for index, url in enumerate(urls):
#         urls_queue.put((index, url))
#     return urls_queue

# # e = prepare_urls('')
# # while e.empty():
# #     e.task_done()

# def create_threads(urls):
#     """"Creates a thread for each url"""
#     print('Starting...')
#     threads = deque()
#     for index, url in enumerate(urls):
#         process = threading.Thread(target=response_handler, args=(url, index))
#         process.setDaemon(True)
#         process.start()
#         threads.append(process)
    
#     for process in threads:
#         process.join()

#     # print('[BS4] Creating soups...')
#     # asyncio.run(main_soup())



# async def test():
#     for i in range(0, 5):
#         print(i)

# async def testa():
#     for i in range(7, 10):
#         print(i)

# async def main():
#     loop = asyncio.get_event_loop()
#     t1 = threading.Thread(target=loop.create_task(test()))
#     t2 = threading.Thread(target=loop.create_task(testa()))
#     loop.run_until_complete([t1, t2])
#     t1.start()
#     t2.start()

# # asyncio.run(main())


# if __name__ == "__main__":
#     # parse = argparse.ArgumentParser(description='Threading scrapper')
#     # parse.add_argument('-u', '--urls', required=True, choices=['a' , 'b'])
#     # parsed_args = parse.parse_args()
#     # urls = ['https://example.com', 'https://example.com']
#     # main_thread = threading.Thread(target=create_threads, args=[urls])
#     # main_thread.start()
#     pass


URLS = [
    'https://example.com',
    'https://example.com',
    'https://example.com'
]

htmls = deque()

def algorithm(index, html):
    print('[BS4] Parsing page...')
    tag = htmls.popleft()
    print(tag.find('title'))
    
def create_soup(func):
    def create_soup(url, **kwargs):
        response = func(url)
        if response is not None:
            print('[COMPLETED] %s' % response.status_code)
            htmls.append(BeautifulSoup(response.text, 'html.parser'))
            time.sleep(5)
    return create_soup

@create_soup
def create_requests(url, **kwargs):
    session = requests.Session()
    request = requests.Request(method='GET', url=url)
    prepared_request = session.prepare_request(request)
    session.headers = {'User-Agent': 'Google Bot'}
    response = session.send(prepared_request)
    if response.status_code == 200:
        print('[REQUEST] %s' % url)
        return response
    return None

def create_threads():
    print('Starting scrapper')
    print('-'*20)
    url_threads = deque()
    for index, url in enumerate(URLS):
        url_thread = threading.Thread(target=create_requests, args=[url], kwargs={'index': index})
        url_thread.start()
        url_threads.append(url_thread)

    # for url_thread in url_threads:
    #     url_thread.join()
    
    # with ThreadPoolExecutor(1) as executor:
    #     results = executor.map(algorithm, htmls)
    #     for result in results:
    #         print (result)

if __name__ == "__main__":
    create_threads()
