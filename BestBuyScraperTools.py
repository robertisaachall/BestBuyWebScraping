import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}
SKUS = []
def scrapeSKU(link):
    webpage = requests.get(link, headers=headers)
    parse = BeautifulSoup(webpage.content, 'html5lib')
    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_name = sku_list.findAll('span',attrs={'class':'sku-value'})
    return sku_name

def scrapeNames(link):
    webpage = requests.get(link, headers=headers)
    parse = BeautifulSoup(webpage.content, 'html5lib')
    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_name = parse.findAll('h4',attrs={'class':'sku-header'})
    return sku_name

def scrapePrice(link):
    webpage = requests.get(link, headers=headers)
    parse = BeautifulSoup(webpage.content, 'html5lib')
    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_price = sku_list.findAll('span',attrs={'class':'sr-only'})
    return sku_price

def scrapeReviews(link):
    webpage = requests.get(link, headers=headers)
    parse = BeautifulSoup(webpage.content, 'html5lib')
    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_rating = sku_list.findAll('p',attrs={'class':'sr-only'})
    return sku_rating

def receiveData(link):
    return

def receivePrint(link,csvFile):
    
    sku_name = scrapeReviews(link)
    for row in sku_name:
        print(row.text)

    
    file = open(csvFile,'w')
    with file:
        writer = csv.writer(file)
        for row in sku_name:
            writer.writerow(row.text)

    print("Printing done. Check the CSV file.")

    return