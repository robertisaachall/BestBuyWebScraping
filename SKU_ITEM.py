class SKU_ITEM:
    def __init__(self,name,sku,price,rating):
        self.name = name
        self.sku = sku
        self.price = price
        self.rating = rating
        #self.numReviews = numReviews

    def returnName(self):
        return self.name
    def returnSKU(self):
        return self.sku
    def returnPrice(self):
        return self.price
    def returnRating(self):
        return self.rating
    

    def display(self):
        print(self.name)
        print(self.sku)
        print(self.price)
        print(self.rating)