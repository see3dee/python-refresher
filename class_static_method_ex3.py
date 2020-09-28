class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        new_store = Store(store.name + " - franchise")
        return new_store

        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return store.name + ', total stock price: ' + str(store.stock_price())
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'


# store1 = Store('Ebay')
# store2 = Store('Amazon')
# store2.add_item('keyboard', 25)
# store2.store_details(store2)
# print(Store.store_details(store2))
# print(Store.store_details(store1))
# store1f = Store.franchise(store2)
# print(store1f.name)





