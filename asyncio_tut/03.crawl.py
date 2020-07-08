import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def get(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        # 모든 정보를 보기 좀 그러니 title만 꺼내보자
        root = BeautifulSoup(html, "html.parser")
        return root.find('title').text

async def get_all(urls):
    coroutines = [get(url) for url in urls]
    responses = await asyncio.gather(*coroutines)
    return responses

if __name__ == '__main__':
    urls = ['http://python.org', 'http://google.com', 'http://daum.net']
    responses = asyncio.run(get_all(urls))
    print(responses)

