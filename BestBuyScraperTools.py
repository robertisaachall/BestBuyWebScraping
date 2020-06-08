import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv




def receiveData(link):
    return

def receivePrint(link):

    headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}

    webpage = requests.get(link, headers=headers)


    parse = BeautifulSoup(webpage.content, 'html5lib')


    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_name = parse.findAll('h4',attrs={'class':'sku-header'})

    for row in sku_name:
        print(row.string)

    return