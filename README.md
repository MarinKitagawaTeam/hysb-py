# hysb-py
A Hypixel Skyblock API Python Wrapper. It will only contain features which are required for the Marin Kitagawa Bot.
This wrapper is fully written in async. Currently, there isn't a documentation. Simply read the source code, if you 
still have any questions, create an Issue or dm me on Discord: Wambo#0800
## Usage
```python
import hysb

async def main():
    # Initialize the client with your api key 
    client = await hysb.Client.connect("<YOUR-API-KEY>")
    # Get the first bazaar item
    item = await client.skyblock.bazaar()[0]
    # print its ID
    print(item.id)
```
