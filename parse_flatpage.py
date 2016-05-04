#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from sqlobject import *


connection_string = 'postgres://r:password@localhost/flats'
connection = connectionForURI(connection_string)
sqlhub.processConnection = connection

class Flat(SQLObject):
    adress = StringCol()
    walls = StringCol()
    price = StringCol()
    area = StringCol()
    living_area = StringCol()
    kitchen_area = StringCol()
    dollar_price = StringCol()
    building_type = StringCol()
    floors_number = IntCol()
    floor = IntCol()
    days = IntCol()
    balcony = IntCol()
    rooms = IntCol()
    code = IntCol()
    updated = StringCol()
    condition = StringCol()

Flat.createTable()

from bs4 import BeautifulSoup
import requests


def scraper():
    File = open('realtylinks.txt', 'r')
    counter = 0
    for line in File.readlines():
        try:
            page = requests.get(line)
            soup = BeautifulSoup(page.content)

            flat = {'Адреса': 'NULL',
                    'Матеріал стін': 'NULL',
                    'Ціна': 'NULL',
                    'Загальна площа': 'NULL',
                    'Житлова площа': 'NULL',
                    'Площа кухні': 'NULL',
                    'Ціна $': 'NULL',
                    'Тип будівлі': 'NULL',
                    'Поверховість': 0,
                    'Поверх': 0,
                    'Днів на сайті': 200000,
                    'Балконів': 100,
                    'Кімнат': 0,
                    'Код': 0,
                    'Оновлено': 'NULL',
                    'Стан': 'NULL'
                    }
            description = soup.title.get_text()
            desc = description.split(": ")
            flat['Адреса'] = desc[1]
            # get features:
            features = soup.find_all("li", class_="col-sm-6 col-dense-left")
            for i in range(len(features)):
                f = features[i].get_text()
                f_list = f.split(": ")
                x = f_list[0]
                if x.strip() in flat:
                    flat[x.strip()] = f_list[1]

            f = Flat(adress=flat['Адреса'].encode('utf-8'), walls=flat['Матеріал стін'].encode('utf-8'),
                     price=flat['Ціна'].encode('utf-8'), area=flat['Загальна площа'].encode('utf-8'),
                     living_area=flat['Житлова площа'].encode('utf-8'), kitchen_area=flat['Площа кухні'].encode('utf-8'),
                     dollar_price=flat['Ціна $'].encode('utf-8'), building_type=flat['Тип будівлі'].encode('utf-8'),
                     floors_number=int(flat['Поверховість']), floor=int(flat['Поверх']),
                     days=int(flat['Днів на сайті']), balcony=int(flat['Балконів']), rooms=int(flat['Кімнат']),
                     code=int(flat['Код']), updated=flat['Оновлено'].encode('utf-8'),
                     condition=flat['Стан'].encode('utf-8'))

        except requests.exceptions.TooManyRedirects:
            pass
        except IndexError:
            pass

        counter +=1
        print counter
    File.close()

scraper()

from sounds import music
music()