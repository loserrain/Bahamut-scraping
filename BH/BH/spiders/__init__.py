# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import bs4
from ..items import BHItem

class BhSpider(scrapy.Spider):
    name = 'BH' #專案名稱
    allowed_domains = ['forum.gamer.com.tw'] #網域名稱
    #start_urls = ['http://forum.gamer.com.tw/B.php?bsn=60076']
   
    def start_requests(self): #開始進行請求
       
        urls =[]
        maxPages =5 #決定要爬多少頁

        for page in range(1,maxPages+1): #先分別建立maxPages頁的網址再一一丟出請求
            urls.append('https://forum.gamer.com.tw/B.php?page='+ str(page)+'&bsn=60076')

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        

      


    def parse(self, response): #利用BS4套件解析頁面
        soup = bs4.BeautifulSoup(response.text, 'lxml')
      
        #titles.get("href") #獲取網址

        '''for link in soup.find_all('p','b-list__brief'):
            print(link.get_text())'''

        items = BHItem()
        
       
        for article in soup.find_all('div','imglist-text'):
            
            artcle_title = article.find('p','b-list__main__title')
            text =  article.find('p','b-list__brief')
            
            
            items['artcle_title'] = artcle_title.get_text()
            items['text'] = text.get_text() 

            yield items
          
        
      
   
    