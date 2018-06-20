from Store import Store
"""
Mocking example
"""


class PurchaseOrder:
    def __init__(self, product_name:str, amount:int)->None:
        self.product_name = product_name
        self.amount = amount

    def buy(self, store:Store)->None:
        if store.are_there_enough_products(self.product_name, self.amount):
            store.remove_products(self.product_name, self.amount)