import requests
import BestBuyScraperTools
import SKU_ITEM
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

URL = 'https://www.bestbuy.com/site/refrigerators/french-door-refrigerators/abcat0901004.c?id=abcat0901004'
items = BestBuyScraperTools.createAndBuildItemList(URL)


BestBuyScraperTools.writeToCsv(items,'BBscraped.csv','a')

#https://www.bestbuy.com/site/refrigerators/french-door-refrigerators/abcat0901004.c?id=abcat0901004
#https://www.bestbuy.com/site/refrigerators/french-door-refrigerators/abcat0901004.c?cp=2&id=abcat0901004