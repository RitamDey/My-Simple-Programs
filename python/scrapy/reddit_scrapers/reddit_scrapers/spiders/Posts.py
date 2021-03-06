# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from reddit_scrapers.items import ImageItem


class PostsSpider(scrapy.Spider):
    name = 'Posts'
    start_urls = ['https://www.reddit.com/r/EarthPorn/']

    def parse(self, response):
        table_xpath = "//div[@id='siteTable']/div"
        href_xpath = "./a/@href"
        title_xpath = "./div[2]/div[@class='top-matter']/p[@class='title']/a/text()"
        next_xpath = "//div[@class='nav-buttons']/span[@class='nextprev']\
        /span[@class='next-button']/a/@href"

        links = response.xpath(table_xpath).xpath(href_xpath)
        next_page = response.xpath(next_xpath).extract_first()

        for link in links:
            link = link.extract()
            if link.find("/r/") != -1:
                yield Request(url=response.urljoin(link), callback=self.parse_post)
            elif link.find("jpg") != -1:
                image = ImageItem()
                image['name'] = link
                image['image_urls'] = [link,]

                yield image

        yield Request(url=next_page, callback=self.parse)

    def parse_post(self, response):
        title_xpath = "//div[@class='top-matter']/p[@class='title']/a/text()"
        picture_xpath = "//div[@class='media-preview-content']/a/@href"

        picture = response.xpath(picture_xpath).extract()
        title = response.xpath(title_xpath).extract_first()

        image = ImageItem()
        image["name"] = title
        image["image_urls"] = picture

        yield image
