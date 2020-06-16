class SKU_ITEM:
    def __init__(self,name,sku,price,rating,numReviews):
        self.name = name
        self.sku = sku
        self.price = price
        self.rating = rating
        self.numReviews = numReviews

    def returnName(self):
        return name
    def returnSKU(self):
        return sku
    def returnPrice(self):
        return price
    def returnRating(self):
        return rating
    def returnNumReviews(self):
        return numReviews

    def display(self):
        print(self.name)
        print(self.sku)
        print(self.price)
        print(self.rating)
        print(self.numReviews)