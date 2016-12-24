import scrapy
import logging
from ..items import RoommatesbudapestSpidersItem


class RoomatesSpider(scrapy.Spider):
    name = 'roomatesspider'
    # allowed_domains = ['']
    start_urls = (
        'http://roommatesbudapest.com/site/roommates',
    )

    def parse(self, response):
        href_last_page = response.xpath('//li[@class="last"]/a/@href').extract_first()
        number_pages = int(href_last_page.rsplit('-')[-1])
        for page in range(1, number_pages + 1):
            url = '%s-%s' % (href_last_page.rsplit('-')[0], page)
            yield scrapy.Request(url, callback=self.parse_pages)

    def parse_pages(self, response):
        for href in response.xpath('//a[text()="view"]/@href').extract():
            url = response.urljoin(href)
            logging.info(url)
            yield scrapy.Request(url, callback=self.parse_room_page)

    def parse_room_page(self, response):
        item = RoommatesbudapestSpidersItem()
        item['type'] = response.xpath('//dt[text()="%s"]/following-sibling::dd/text()' % 'Type:').extract_first()
        item['city'] = response.xpath('//dt[text()="%s"]/following-sibling::dd/text()' % 'City:').extract_first()
        item['address'] = response.xpath('//dt[text()="%s"]/following-sibling::dd/text()' % 'Address:').extract_first()
        item['zip_code'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Zip code:').extract_first()
        item['rent_price_of_the_room'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Rent price of the room:').extract_first()
        item['deposit'] = response.xpath('//dt[text()="%s"]/following-sibling::dd/text()' % 'Deposit:').extract_first()
        item['room_size'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Room size:').extract_first()
        item['apartment_size'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Apartment size:').extract_first()
        item['total_number_of_flatmates'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Total number of flatmates:').extract_first()

        item['available_from'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Available from:').extract_first()
        item['term_of_lease'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Term of lease:').extract_first()
        item['apartment_condition'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Apartment condition:').extract_first()
        item['floor'] = response.xpath('//dt[text()="%s"]/following-sibling::dd/text()' % 'Floor:').extract_first()
        item['elevator'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Elevator:').extract_first()
        item['numbers_bathrooms_or_showers'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'No. Bathrooms/Showers:').extract_first()
        item['numbers_of_toilets'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'No. Toilets:').extract_first()
        item['close_to_or_metro_or_tram'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Close to metro/tram:').extract_first()
        item['distance_to_public_transport'] = response.xpath(
            '//dt[text()="%s"]/following-sibling::dd/text()' % 'Distance to public transport:').extract_first()
        item['environment_surroundings'] = [i.extract() for i in response.xpath(
            '//div[@id="%s"]/ul/descendant::*/text()' % 'surrounding-list')]

        item['latitude'] = ''
        item['longitude'] = ''

        item['age'] = response.xpath(
            '//ul[@class="list tab-aboutme"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Age').extract_first()
        item['gender'] = response.xpath(
            '//ul[@class="list tab-aboutme"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Gender').extract_first()
        item['studies_at'] = response.xpath(
            '//ul[@class="list tab-aboutme"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Study at:').extract_first()

        item['hobbies_interest'] = response.xpath(
            '//ul[@class="list tab-aboutme"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Hobbies/Interest').extract_first()
        item['languages'] = response.xpath(
            '//ul[@class="list tab-aboutme"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Languages').extract_first()
        item['my_roommates_age'] = response.xpath(
            '//ul[@class="list tab-aboutroommate"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Age').extract_first()
        item['my_roommates_gender'] = response.xpath(
            '//ul[@class="list tab-aboutroommate"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Gender').extract_first()
        item['my_roommates_occupation'] = response.xpath(
            '//ul[@class="list tab-aboutroommate"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Occupation').extract_first()
        item['my_roommates_smoking'] = response.xpath(
            '//ul[@class="list tab-aboutroommate"]/li/dl/dt[text()="%s"]/following-sibling::dd/text()' % 'Smoking').extract_first()

        yield item
