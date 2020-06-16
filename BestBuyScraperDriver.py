import requests
import BestBuyScraperTools
import SKU_ITEM
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

URL = 'https://www.bestbuy.com/site/small-appliances/coffee-tea-espresso/pcmcat367400050002.c?id=pcmcat367400050002'
BestBuyScraperTools.receivePrint(URL,'BBscraped.csv')

 