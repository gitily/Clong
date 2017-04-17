class Item(object):

    def __init__(self, price=1):
        self._price = price

    @property
    def price(self):
        print "get_price has been called"
        return self._price

    @price.setter
    def price(self, new_price):
        print "set_price has been called"
        self._price = new_price

guitar = Item(300)

guitar.price = 200
print guitar.price

