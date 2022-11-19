from hysb.connectors.base_connector import get, post
from hysb.models import *

import aiohttp
import hysb.utils as utils


class SkyblockConn:

    def __init__(self, session: aiohttp.ClientSession):
        self.session: aiohttp.ClientSession = session

    async def collections(self) -> Collections:
        """Returns information regarding Collections in Skyblock"""
        data = await get(self.session, utils.COLLECTIONS)
        return Collections(data)

    async def election_mayor(self) -> ElectionMayorResult:
        """Information regarding the current mayor and ongoing election in SkyBlock"""
        data = await get(self.session, utils.ELECTION_MAJOR)
        return ElectionMayorResult(data)

    async def bazaar(self):
        """Returns the list of products along with their sell summary, buy summary and quick status."""
        data = await get(self.session, utils.BAZAAR)
        return Bazaar(data)
