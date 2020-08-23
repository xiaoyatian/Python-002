# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter


class SpidersPipeline:
    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        release_date = item['release_date']
        output = f'|{title}|\t|{movie_type}|\t|{release_date}|\n\n'
        with open('./doubanmovie.txt', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
