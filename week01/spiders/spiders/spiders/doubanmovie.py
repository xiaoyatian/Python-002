import scrapy
from spiders.items import SpidersItem
from scrapy.selector import Selector

class DoubanmovieSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # 起始URL列表
    start_urls = ['https://movie.douban.com/top250']

    def start_requests(self):

        url = 'https://movie.douban.com/top250'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)


    # 解析函数
    def parse(self, response):
        # 打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)

        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movies = Selector(response=response).xpath('//div[@class="hd"]')
        for i in range(10):
        #for movie in movies:
        #     title = i.find('a').find('span',).text
        #     link = i.find('a').get('href')
            # 路径使用 / .  .. 不同的含义　
            item = SpidersItem ()
            title = movies[i].xpath('./a/span/text()')
            link = movies[i].xpath('./a/@href')
            print('---------')
            print('num::{i}')
            print(title)
            # print(link)
            print('----------')
            title2 = title.extract()
            print(f'title::{title2}')
            print(f'link::{link.extract()}')
            print(f'title_first:::{title.extract_first()}')
            print(f'link_first:::{link.extract_first()}')
            print(f'title_first:::::::::{title.extract_first().strip()}')
            print(f'link_first::::::::::{link.extract_first().strip()}')
            item['title'] = title.extract_first().strip()
            item['link'] = link.extract_first().strip()
            yield scrapy.Request(url=link.extract_first().strip(), meta={'item': item}, callback=self.parse2)

    # 解析具体页面
    def parse2(self, response):
        item = response.meta['item']
        
        
        infos = Selector(response=response).xpath('//*[@id="info"]')
        for info in infos:
            genres = info.xpath('./span[@property="v:genre"]/text()')
            initialReleaseDates = info.xpath('./span[@property="v:initialReleaseDate"]/text()')
            # movie_type3 = Selector(response=response).xpath('//*[@id="info"]/span[7]').extract_first().strip()
            # release_date = Selector(response=response).xpath('//*[@id="info"]/span[11]').extract_first().strip()
       
            # movie_type=f'{movie_type1}/{movie_type2}/{movie_type3}'


            genre=[]
            release_date=[]
            for genre1 in genres:

                print('==========')
                genre2=genre1.extract().strip()
                print(genre2)
                genre.append(genre2)
                
            for initialReleaseDate in initialReleaseDates:
                print('==========')
                release_date2=initialReleaseDate.extract().strip()
                print(release_date2)
                release_date.append(release_date2)
            
            print('==========')
            print('==========')
            print(genre)
            print(release_date)
            item['movie_type'] = genre
            item['release_date'] = release_date
            yield item
