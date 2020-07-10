import scrapy

class OpggSpider(scrapy.Spider):
	name = "opgg"

	start_urls = [
		'https://na.op.gg/summoner/userName=Epicluke0328'
	]

	def parse(self, response):
		player = response.url.split('=')[-1]
		filename = 'player-%s.html' % player
		with open(filename, 'wb') as file:
			file.write(response.body)