# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# scraped data-->item containers-->csv/json files
# scraped data-->item containers-->pipelines-->SQL/Mongo database

import mysql.connector

class SmartstudysitePipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'ashi123456',
            database = 'datas'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""drop table if exists data_tb""")
        self.curr.execute("""create table data_tb(
                            topic text,
                            content text
                            )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute("""insert into data_tb values(%s,%s)""",(
                        item['topic'],
                        item['content']
        ))
        self.conn.commit()