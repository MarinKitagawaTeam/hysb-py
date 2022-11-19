import aiohttp
import asyncio
import logging

logger = logging.Logger(__name__)


class Client:

    def __init__(self, token: str = None) -> None:
        self.token = token
        self._auth = {"ApiKey": token}
        self._session = aiohttp.ClientSession()

    async def validate_token(self):
        if not self.token:
            logger.warning("YOU DIDN'T PROVIDE A TOKEN, YOU CAN ONLY USE ENDPOINTS WHICH DON'T REQUIRE AUTHORIZATION! "
                           "MORE INFORMATION UNDER: https://api.hypixel.net/")
            return

        async with aiohttp.ClientSession() as session:
            async with session.get('')

