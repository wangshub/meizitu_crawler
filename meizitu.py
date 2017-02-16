#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import os
from Download import request
from pymongo import MongoClient

class meizitu():
    def __init__(self):
        print 'hello'
    #
    def all_url(self, url):
        html = request.get(url, 3)
        all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
        for a in all_a:
            title = a.get_text()
            print 'Saving... ', title
            # path = str(title).decode('utf-8').replace('?','_')
            path = (title)
            self.mkdir(path)
            os.chdir('/media/wangs/Docs/pic/'+path)
            href = a['href']
            self.html(href)
    #
    # def html(self, herf):
    #     html = request.get(herf, 3)
    #     max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[10].get_text()
    #     for page in range(1, int(max_span+1)):
    #         page_url = href + '/' + page
    #         self.img(page_url)
    def html(self, href):
        html = request.get(href, 3)
        max_span = BeautifulSoup(html.text, 'lxml').find_all('span')[10].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)
    #
    def save(self, img_url):
        name = img_url[-9:-4]
        print('save img', img_url)
        img = request.get(img_url, 3)
        f = open(name+'.jpg','ab')
        f.write(img.content)
        f.close()

    #
    # def img(self, page_url):
    #     img_html = request.get(page_url, 3)
    #     img_url = BeautifulSoup(img_html, 'lxml').find('div', class_='main-image').find('img')['src']
    #     self.save(img_url)
    def img(self, page_url):
        img_html = request.get(page_url, 3) ##这儿更改了一下（是不是发现  self 没见了？）
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    #
    def mkdir(self, path):
        path = path.strip()
        isExist = os.path.exists(os.path.join("/media/wangs/Docs/pic", path))
        if isExist:
            print 'file already exist'
            return True
        else :
            os.mkdir(os.path.join("/media/wangs/Docs/pic", path))
            return True

meizi = meizitu()
meizi.all_url("http://www.mzitu.com/all")
