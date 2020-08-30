# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import pymysql.cursors
class SpidersPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='127.0.0.1',#数据库地址
            port=3306,# 数据库端口
            db='test', # 数据库名
            user = 'root', # 数据库用户名
            passwd='rootroot', # 数据库密码
            charset='utf8', # 编码方式
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()





    def process_item(self, item, spider):
        title = item['title']
        movie_type = item['movie_type']
        release_date = item['release_date']
        # output = f'{title},{movie_type},{release_date}\n\n'
        # with open('./doubanmovie.csv', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        self.cursor.execute(
            """insert into douban(title, movie_type, release_date)
            value (%s, %s, %s)""",
            (''.join(title),
             '/'.join(movie_type),
             '/'.join(release_date)))

        # 提交sql语句
        self.connect.commit()


        return item
