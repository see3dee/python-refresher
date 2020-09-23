class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    # def stock_price(self):
    #     total = 0
    #     for item in self.items:
    #         total += item['price']
    #     return total

# list comprehension is useful here!  sweet!
    def stock_price(self):
        total = sum([item['price'] for item in self.items])
        return total

#  testing
store = Store('Safeway')
print(store.name)

store.add_item('butter', 4.99)
store.add_item('milk', 1.99)
store.add_item('cheese', 2.99)

print(store.items)
print(store.items[0])
print(len(store.items))

print(f' stock_price is {store.stock_price()}')



