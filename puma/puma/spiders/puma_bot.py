import scrapy

from ..items import PumaItem
import numpy as np

class PumaBotSpider(scrapy.Spider):
    def __init__(self):
        self.count=0
    name = "puma_bot"
    allowed_domains = ["flipkart.com"]
    
    start_urls = ["https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&param=1112&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlJlYWxtZSBzbWFydHBob25lcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=23.productCard.PMU_V2_23&page="+str(i) for i in range(1,50)]

    def parse(self, response):
        self.count+=1
        itemss = PumaItem()
        for j in response.css("._2kHMtA"):
        # j=response    ._4rR01T , ._2GoDe3+ .col-12-12 ._2kHMtA
            itemss["name"] = j.css("div._4rR01T::text").get(default=np.NaN).replace(",","")
            itemss["price"] = j.css("._1_WHN1::text").get(default=np.NaN).replace(",","")
            itemss["rateing"] = j.css("._3LWZlK::text").get(default=np.NaN)
            itemss["ram"] = j.css(".rgWa7D:nth-child(1)::text").get(default=np.NaN)
            itemss["battry"]= j.css(".rgWa7D:nth-child(4)::text").get(default=np.NaN)
            itemss["dispaly"]= j.css(".rgWa7D:nth-child(2)::text").get(default=np.NaN)
            itemss["processer"] =j.css(".rgWa7D:nth-child(5)::text").get(default=np.NaN)
            itemss["camra"] = j.css(".rgWa7D:nth-child(3)::text").get(default=np.NaN)
            itemss["pg"]=self.count
            # itemss["org_price"] = j.css("._27UcVY::text").getall()

        # pd.DataFrame(itemss).to_csv("data_.csv",index=False)
        # for i,j in itemss["name"]:
            # print(i,j)
            yield itemss
        # next_page = response.css("._1LKTO3 span ::attr(href)").get(default=np.NaN)
        # if next_page is not None:
        #     yield response.follow(next_page, self.parse)