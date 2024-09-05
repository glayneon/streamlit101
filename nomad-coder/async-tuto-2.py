import requests
import time
import aiohttp
import asyncio

start_time = time.time()

def fetch(url):
    return requests.get(url).text

page1 = fetch('http://example.com')
page2 = fetch('http://example.org')

print(f"Done in {time.time() - start_time} seconds.")

async def fetch_async(url, session):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        page1 = asyncio.create_task(fetch_async('http://example.com', session))
        page2 = asyncio.create_task(fetch_async('http://example.org', session))
        await asyncio.gather(page1, page2)

start_time = time.time()
asyncio.run(main())

print(f"Done in {time.time() - start_time} seconds.")
