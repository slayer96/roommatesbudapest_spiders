# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RoommatesbudapestSpidersItem(scrapy.Item):
    type = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    zip_code = scrapy.Field()
    rent_price_of_the_room = scrapy.Field()
    deposit = scrapy.Field()
    room_size = scrapy.Field()
    apartment_size = scrapy.Field()
    total_number_of_flatmates = scrapy.Field()
    available_from = scrapy.Field()
    term_of_lease = scrapy.Field()
    apartment_condition = scrapy.Field()
    floor = scrapy.Field()
    elevator = scrapy.Field()
    numbers_bathrooms_or_showers = scrapy.Field()
    numbers_of_toilets = scrapy.Field()
    close_to_or_metro_or_tram = scrapy.Field()
    distance_to_public_transport = scrapy.Field()
    environment_surroundings = scrapy.Field()

    latitude = scrapy.Field()
    longitude = scrapy.Field()

    description = scrapy.Field()
    roommate_type = scrapy.Field()
    in_districts = scrapy.Field()
    budget_between = scrapy.Field()

    age = scrapy.Field()
    gender = scrapy.Field()
    studies_at = scrapy.Field()
    hobbies_interest = scrapy.Field()
    languages = scrapy.Field()
    my_roommates_age = scrapy.Field()
    my_roommates_gender = scrapy.Field()
    my_roommates_occupation = scrapy.Field()
    my_roommates_smoking = scrapy.Field()