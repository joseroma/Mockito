
import unittest
from unittest.mock import MagicMock

from PurchaseOrder import PurchaseOrder
from Store import Store


class TestMethods(unittest.TestCase):

    def test_should_buy_remove_the_product_in_the_store_if_there_are_enough_items(self):
        # Creating the mock object
        store:Store = MagicMock()

        # Stubbing
        store.are_there_enough_products.return_value = True

        # Execute
        purchase_order:PurchaseOrder = PurchaseOrder("Bread", 15)
        purchase_order.buy(store)

        # Verify
        store.remove_products.assert_called_once_with("Bread", 15)
        #store.remove_products.assert_not_called("Pork", 12)

    def test_should_buy_not_remove_the_product_in_the_store_if_there_are_not_enough_items(self):
        # Creating the mock object
        store:Store = MagicMock()

        # Stubbing
        store.are_there_enough_products.return_value = False

        # Execute
        purchase_order:PurchaseOrder = PurchaseOrder("Bread", 15)
        purchase_order.buy(store)

        # Verify
        store.remove_products.assert_not_called()

    def test_shouldBuyWorkIfThereAreProductsTheFirstTimeButNotTheSeconeOne(self):
        # To be implemented
        pass

