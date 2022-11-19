import asyncio
import cfg
import hysb
import logging


logger = logging.Logger(__name__)


async def main():
    client = await hysb.Client.connect(cfg.KEY)
    result = await client.skyblock.election_mayor()
    print(result.mayor.name)

asyncio.run(main())
