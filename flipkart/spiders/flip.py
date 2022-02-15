import scrapy
from ..items import FlipkartItem

class FlipSpider(scrapy.Spider):
    name = 'flip'
    page_no = 2
    # allowed_domains = ['flipkart.com']
    start_urls = [
        'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_7_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_92RED14GXPXF_wp3&fm=neo%2Fmerchandising&iid=M_2d5790a0-d94a-40db-a529-bf2c3d2522ec_3.92RED14GXPXF&ppt=clp&ppn=mobile-phones-store&ssid=was5bwntq80000001644170686284&page=1'

    ]

    def parse(self, response):
        all_phones = response.css('div._2kHMtA')
        items =FlipkartItem()


        for phone in all_phones:

            name = phone.css('div.CXW8mj img::attr(alt)').getall()
            image = phone.css('div.CXW8mj img::attr(src)').getall()
            price = phone.css('div._30jeq3._1_WHN1::text').getall()

            items['name'] = name
            #items['image'] = image
            items['price'] = price
            #if items.name==''


            yield items
        next_page = 'https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DApple&otracker=clp_metro_expandable_7_3.metroExpandable.METRO_EXPANDABLE_Shop%2BNow_mobile-phones-store_92RED14GXPXF_wp3&fm=neo%2Fmerchandising&iid=M_2d5790a0-d94a-40db-a529-bf2c3d2522ec_3.92RED14GXPXF&ppt=clp&ppn=mobile-phones-store&ssid=was5bwntq80000001644170686284&'+str(FlipSpider.page_no)+'/'
        if FlipSpider.page_no <=10:
            FlipSpider.page_no +=1
            yield response.follow(next_page, callback=self.parse)


