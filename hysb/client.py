import asyncio
import aiohttp
import hysb.utils as utils
import logging


logger = logging.Logger('hysb')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


class Client:

    def __init__(self, key: str = None) -> None:
        self.key = key
        self._auth = {"API-Key": key}
        #  TODO implement on_exit function to close session
        self.session = aiohttp.ClientSession(headers=self._auth)

    @classmethod
    async def connect(cls, key: str = None):
        self = cls(key)
        await self._validate_token()
        logger.info(msg="Successfully connected to the Hypixel API")

        return self

    async def _validate_token(self):
        """Private function to validate the API-Key"""
        if not self.key:
            logger.warning("YOU DIDN'T PROVIDE A KEY, YOU CAN ONLY USE ENDPOINTS WHICH DON'T REQUIRE AUTHORIZATION! "
                           "MORE INFORMATION UNDER: https://api.hypixel.net/")
            return

        async with self.session.get(utils.API_KEY_INFORMATION) as resp:
            json = await resp.json()

        if not json['success']:
            raise utils.InvalidApiKey("Please enter a valid API-Key. More information: "
                                      "https://api.hypixel.net/#section/Authentication/ApiKey")
