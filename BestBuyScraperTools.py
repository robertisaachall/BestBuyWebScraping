import requests
import SKU_ITEM
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"}
def scrapeSKU(link):
    webpage = requests.get(link, headers=headers)
    parse = BeautifulSoup(webpage.content, 'html5lib')
    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_name = sku_list.findAll('span',attrs={'class':'sku-value'})


    #Below is the code to filter out the SKUS for the items.
    #Whenever it scrapes the website, it grabs both the model number,
    #and the sku. However we only need the SKU so it grabs the odd numbered indexes.
    counter = 0
    cleaned_skus = []
    for sku in sku_name:
        if(counter == 0):
            counter = counter + 1
            continue
        elif(counter % 2 == 0):
            counter = counter + 1
            continue
        else:
            counter = counter + 1
            cleaned_skus.append(sku.text)

    return cleaned_skus

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


    #Below is cleaning methods. Sometimes garbage such as "selected"
    #gets included in the output. Filtering this is necessary. It also trims
    #the "Your price for this item is: " piece to just have a price.
    cleaned_list = []
    for price in sku_price:
        if(price.text == "selected"):
            continue
        else:
            cleaned_price = price.text.replace("Your price for this item is ","")
            cleaned_list.append(cleaned_price)


    return cleaned_list

def scrapeReviews(link):
    webpage = requests.get(link, headers=headers)
    parse = BeautifulSoup(webpage.content, 'html5lib')
    sku_list = parse.find('ol', attrs={'class':'sku-item-list'})
    sku_rating = sku_list.findAll('p',attrs={'class':'sr-only'})
    return sku_rating

def createAndBuildItemList(link):
    skus = scrapeSKU(link)
    prices = scrapePrice(link)
    names = scrapeNames(link)
    reviews = scrapeReviews(link)
    items = []
    counter = 0
    for iter in skus:
        item = SKU_ITEM.SKU_ITEM(names[counter].text,skus[counter],prices[counter],reviews[counter].text)
        items.append(item)
        counter = counter + 1
    return items

def receivePrint(link,csvFile):
    
    sku_name = scrapeSKU(link)
    for row in sku_name:
        print(row)

    
    file = open(csvFile,'w')
    with file:
        writer = csv.writer(file)
        for row in sku_name:
            writer.writerow(row)

    print("Printing done. Check the CSV file.")

    return