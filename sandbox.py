class ListMethods:
    def __init__(self, lst):
        self.lst = lst

    def lst_sum(self):
        return sum(self.lst)

    def lst_len(self):
        return len(self.lst)

    def lst_ave(self):
        return sum(self.lst)/len(self.lst)


ls = [2, 4, 5, 6, 7]

thing = ListMethods(ls)

print(thing.lst_sum())
print(thing.lst_len())
print(thing.lst_ave())