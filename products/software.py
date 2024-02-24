from products.product import Product


class Software(Product):
    def __init__(self, product_id, product_name, product_retail_price, product_description,software_license):
        super().__init__(product_id, product_name, product_retail_price, product_description)
        self.__software_license = software_license

    def get_software_license(self):
        return self.__software_license

    def set_software_license(self, software_license):
        self.__software_license = software_license
