import asyncio
import cfg
import hysb
import logging


logger = logging.Logger(__name__)


async def main():
    client = await hysb.Client.connect(cfg.KEY)
    api_key_info = await client.hypixel.api_key_information()
    uuid = api_key_info.get('record').get('owner')
    result = await client.skyblock.profiles(uuid)
    item = result.profile
    print(item)

asyncio.run(main())
