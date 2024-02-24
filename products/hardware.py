from products.product import Product
from taxable.taxable import Tax


class Hardware(Tax, Product):
    VAT = 14

    def __init__(self, product_id, product_name, product_retail_price, product_description,hardware_warranty_period):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__hardware_warranty_period = hardware_warranty_period

    def get_hardware_warranty_period(self):
        return self.__hardware_warranty_period

    def set_hardware_warranty_period(self,hardware_warranty_period):
        self.__hardware_warranty_period = hardware_warranty_period


    def get_tax(self, amount):
        return amount * Tax.VAT / 100

