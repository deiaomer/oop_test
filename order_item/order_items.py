from datetime import datetime

from products.hardware import Hardware


class OrderItem:
    LINE_NO = 1

    def __init__(self, product_obj, quantity):
        self.__product_obj = product_obj
        self.__quantity = quantity
        self.__line_no = OrderItem.LINE_NO
        self.__order_list = []
        OrderItem.LINE_NO = OrderItem.LINE_NO + 1


    def get_line_no(self):
        return self.__line_no

    def get_product(self):
        return self.__product_obj

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self,x):
        self.__quantity =  x

    def get_unit_price(self):
        return self.__product_obj.get_unit_price()

    def get_product_tax(self):
        if isinstance(self.__product_obj , Hardware):
            amount = self.__product_obj.get_unit_price() * self.__quantity
            return self.__product_obj.get_tax(amount)
        else:
            return 0

    def get_items_total(self):
        return self.__quantity * self.__product_obj.get_unit_price() + self.get_product_tax()






