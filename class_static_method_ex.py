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

    # def __repr__(self):
    #     return f"{self.name}, total stock price: {self.stock_price()}"

    @classmethod
    def franchise(cls, store):
        Store(store.name)
        new_store.name = f"{name} - franchise"
        return new_store
        # Return another store, with the same name as the argument's name, plus " - franchise"

    # @staticmethod
    # def store_details(store):
    #     return f"{store.name}, total stock price: {store.stock_price()}"
    #     # Return a string representing the argument
    #     # It should be in the format 'NAME, total stock price: TOTAL'

print(Store)
store1 = Store('safeway')
print(store1)
store1.add_item('apple', 2)
print(store1.stock_price())
print(store1.items)
print(Store.franchise('test').name)
print(Store.store_details(store1))
