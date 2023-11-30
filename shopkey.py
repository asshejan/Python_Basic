class shopping:

    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {'item' : item, 'price' : price, 'quantity' : quantity}
        self.cart.append(product)

    def remove_item(self, item):
        for product in self.cart:
            if product['item'] == item:
                print('found')
                self.cart.remove(product)
                break
            else:
                print(f'{item} not found in the list')
    
    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']
        print('total price', total)
        print('exchange =', amount-total)


swapon = shopping('Alan Swapon')
swapon.add_to_cart('Mula', 30, 2)
swapon.add_to_cart('Alu', 20, 5)
swapon.add_to_cart('Begun', 40, 3)

swapon.remove_item('Mula')
swapon.checkout(600)