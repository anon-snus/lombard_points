import random
from utils import *
from config import *
from scrapper import Scrapper
import asyncio

async def main():
    scrapper = Scrapper(proxy=PROXY)

    with open('wallets.txt', 'r') as f:
        wallets = f.read().splitlines()

    for wallet in wallets:
        if PROXY:
            q = await change_ip(CHANGE_IP_LINK)
            print(f'Changing IP: {q}')
        wallet_data = await scrapper.parse(wallet)
        print(wallet_data)
        await asyncio.sleep(random.randint(25, 50))

if __name__ == '__main__':
    asyncio.run(main())
