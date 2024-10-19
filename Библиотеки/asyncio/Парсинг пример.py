import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = 'https://example.com'  # Замените на URL страницы, которую хотите спарсить
    html = await fetch_page(url)
    print(html)


asyncio.run(main())
