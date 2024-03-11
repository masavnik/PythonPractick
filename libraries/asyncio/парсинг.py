import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        texts = await asyncio.gather(*[
            fetch(session, url) for url in urls
        ])
        return texts


years_to_fetch = [f'https://en.wikipedia.org/wiki/{year}' for year in range(1990, 2020)]

asyncio.run(fetch_all(years_to_fetch))
