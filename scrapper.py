import asyncio
from utils import async_get, change_ip

class Scrapper:
	def __init__(self, proxy):
		self.proxy = proxy

	async def parse(self, wallet:str):
		url = f'https://mainnet.prod.lombard.finance/api/v1/referral-system/season-1/points/{wallet}'

		for i in range(5):
			try:
				res = await async_get(url=url, proxy=self.proxy)
				return {wallet: res.get('total')}

			except Exception as e:
				print(e)
				await asyncio.sleep(1)


