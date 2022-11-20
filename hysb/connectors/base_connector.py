import aiohttp
import typing


async def get(session: aiohttp.ClientSession, url: str, query: str = "") -> typing.Dict:
    async with session.get(url + '?' + query) as resp:
        json = await resp.json()
        return json


async def post(session: aiohttp.ClientSession, url: str, body: dict) -> typing.Dict:
    async with session.post(url=url, data=body) as resp:
        json = await resp.json()
        return json

