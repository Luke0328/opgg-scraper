# Scrapy Spider that extracts statistics (i.e. win rate) for a Summoner's 7 most played Champions. 
# Data is scraped from website op.gg. 

import scrapy
from ..items import Champion

class OpggSpider(scrapy.Spider):
	name = "opgg"

	start_urls = [
		'https://na.op.gg/summoner/userName=Epicluke0328'
	]

	def parse(self, response):

		root = response.xpath("//div[@class='MostChampionContent']")
		
		for i in range(7):

			champion_name = root.xpath(".//div[@class='ChampionName']/a/text()").getall()[i].strip()

			average_cspm = root.xpath(
				".//div[@class='ChampionMinionKill tip']/text()").getall()[i].strip().split()[2].replace("(", "").replace(")", "")

			kda = root.xpath(".//span[@class='KDA']/text()").getall()[i]

			win_ratio = root.xpath(".//div[@title='Win Ratio']/text()").getall()[i].strip()

			games_played = root.xpath(".//div[@class='Title']/text()").getall()[i].replace(" Played", "")

			champion = Champion()

			champion["champion_name"] = champion_name
			champion["average_cspm"] = average_cspm
			champion["kda"] = kda
			champion["win_ratio"] = win_ratio
			champion["games_played"] = games_played

			yield champion