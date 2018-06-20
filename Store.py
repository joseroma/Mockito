""" Interface representing a store

"""


class Store:
    def are_there_enough_products(self, product_name:str, amount:int)->bool:
        pass

    def remove_products(self, product_name:str, amount:int)->bool:
        pass