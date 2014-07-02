# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http.request import Request
from tutorial.items import TutorialItem
from scrapy.selector import Selector

items=[]


#http://www.flipkart.com/moto-g/product-reviews/ITMDSMBXCRM9WY8R?pid=MOBDSGU2QFWMHGRR&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=30

class TutorialSpider(scrapy.Spider):
    name = 'flipkart'
    allowed_domains = ['http://www.flipkart.com']
        
    start_urls = ['http://www.flipkart.com/moto-g/product-reviews/ITMDSMBXCRM9WY8R?pid=MOBDSGU2QFWMHGRR&rating=1,2,3,4,5&reviewers=all&type=all&sort=most_helpful&start=%d' %n for n in range(10, 1300, 10)]
    
    

    def parse(self, response):
        
        for sel in response.xpath('//span[@class="review-text"]'):
            
            item = TutorialItem()
            item['review'] = sel.xpath('text()').extract()
	    items.append(item)
	return items
	
	






   


        
        

        
            


