import asyncio
import cfg
import hysb
import logging


logger = logging.Logger(__name__)


async def main():
    client = await hysb.Client.connect(cfg.KEY)
    result = await client.skyblock.bazaar()
    item = result.products[0]
    print(item.id)

asyncio.run(main())
