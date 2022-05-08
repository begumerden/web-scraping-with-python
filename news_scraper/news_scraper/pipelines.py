# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface

from datetime import datetime

class NewsScraperPipeline:
    def process_item(self, item, spider):
        #  "date": "2022-04-25T18:55:18.000Z"
        d = item['date'].split('T')[0]
        item['date'] = datetime.strptime(d, '%Y-%m-%d').strftime('%d-%m-%Y')
        return item
