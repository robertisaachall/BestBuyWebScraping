import BestBuyScraperTools
from datetime import datetime

search_term = "hello"
URL = 'https://www.bestbuy.com/site/searchpage.jsp?st=' + search_term
items = BestBuyScraperTools.createAndBuildItemList(URL)

current_time = datetime.now()
current_time = current_time.strftime("%H-%M-%S")
test_number = "BBScrap_test_" + str(current_time) + ".csv"

BestBuyScraperTools.writeToCsv(items, test_number, 'w')
