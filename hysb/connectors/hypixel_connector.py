from hysb.connectors.base_connector import get, post

import aiohttp
import hysb.utils as utils


class HypixelConn:

    def __init__(self, session: aiohttp.ClientSession):
        self.session: aiohttp.ClientSession = session

    async def api_key_information(self) -> dict:
        """Returns information regarding Collections in Skyblock"""
        data = await get(self.session, utils.API_KEY_INFORMATION)
        return data
