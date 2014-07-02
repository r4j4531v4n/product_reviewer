from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log, signals
from spiders.dmoz_spider import TutorialSpider
from scrapy.xlib.pydispatch import dispatcher
from textblob import TextBlob
import csv

pos=0
neg=0

def stop_reactor():
	reactor.stop()
	dispatcher.connect(stop_reactor, signal=signals.spider_closed)
	settings = get_project_settings()
	settings.overrides['FEED_URI'] = 'reviews.csv'
	settings.overrides['FEED_FORMAT'] = 'csv'
	spider = TutorialSpider(domain='www.flipkart.com')
	crawler = Crawler(settings())
	crawler.configure()
	crawler.crawl(spider)
	crawler.start()
	log.start(loglevel=log.DEBUG)
	log.msg("------------>Running reactor")
	result = reactor.run()
	print result
	log.msg("------------>Running stoped")
	
	
with open('reviews.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='"', quoting=csv.QUOTE_ALL)
	for row in spamreader:
		test=TextBlob(' '.join(row))
		score=test.sentiment
		if round(score[0] ,2) > 0.00:
			pos+=1
		else:
			neg+=1
			

print "Percentage of positive response "+round((100*pos/(pos+neg)),2)