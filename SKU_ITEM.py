class SKU_ITEM:
    def __init__(self,name,sku,price,rating):
        self.name = name
        self.sku = sku
        self.price = price
        self.rating = rating
        #self.numReviews = numReviews

    def returnName(self):
        return name
    def returnSKU(self):
        return sku
    def returnPrice(self):
        return price
    def returnRating(self):
        return rating
    

    def display(self):
        print(self.name)
        print(self.sku)
        print(self.price)
        print(self.rating)