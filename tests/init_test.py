import asyncio
import cfg
import hysb
import logging


logger = logging.Logger(__name__)


async def main():
    client = await hysb.Client.connect(cfg.KEY)

asyncio.run(main())
