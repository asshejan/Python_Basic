class Shop:

    mall = 'Jamuna'
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


mehzaben = Shop('Mehazabeen')
mehzaben.add_to_cart('shoes')
mehzaben.add_to_cart('bag')
print("mehjabeen cart =", mehzaben.cart)

niso = Shop('arfan nisho')
niso.add_to_cart('cap')
niso.add_to_cart('glass')
print("nisho cart=", niso.cart)

apurbo = Shop('apurbo vai')
apurbo.add_to_cart('chiruni')
print("apurbo cart =", apurbo.cart)