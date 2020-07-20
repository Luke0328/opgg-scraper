import scrapy
from ..items import Champion

class OpggSpider(scrapy.Spider):
	name = "opgg"

	start_urls = [
		'https://na.op.gg/summoner/userName=Epicluke0328'
	]

	def parse(self, response):

		most_played = response.xpath("//div[@class='MostChampionContent']")
		
		for i in range(7):
			champion_name = most_played.xpath(".//div[@class='ChampionName']/a/text()").getall()[i].strip()

			average_cspm = most_played.xpath(
				".//div[@class='ChampionMinionKill tip']/text()").getall()[i].strip().split()[2].replace("(", "").replace(")", "")

			kda = most_played.xpath(".//span[@class='KDA']/text()").getall()[i]

			win_ratio = most_played.xpath(".//div[@title='Win Ratio']/text()").getall()[i].strip()

			games_played = most_played.xpath(".//div[@class='Title']/text()").getall()[0].replace(" Played", "")

