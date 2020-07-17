# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Champion(scrapy.Item):
    champion_name = scrapy.Field()
    cspm = scrapy.Field()
    kda = scrapy.Field()
    win_ratio = scrapy.Field()
    games = scrapy.Field()
    
