#!/bin/bash

import requests
import asyncio

async def scrapper(url):
    response = requests.get(url)
    if response.status_code == 200:
        requests.post('http://localhost:4000/', data=response.text)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(scrapper('http://example.com'))
    loop.close()
    # asyncio.run(scrapper('http://example.com'))