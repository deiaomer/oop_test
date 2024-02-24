from datetime import datetime

from order_item.order_items import OrderItem


class Order:

    def __init__(self, customer, order_id):
        self.__order_customer = customer
        self.__order_id = order_id
        self.__order_date = datetime.now().date()
        self.__order_total = 0
        self.__order_list = []

    def get_order_id(self):
        return self.__order_id

    def get_order_customer(self):
        return self.__order_customer

    def get_order_date(self):
        return self.__order_date

    def print_final_invoice(self):
        return self.__order_id

    def print_list(self):
        return self.__order_list

    def add_to_cart(self, product_obj, qty):
        checking = False
        for item in self.__order_list:

            if product_obj.get_product_id() == item.get_product().get_product_id():
                item.set_quantity(item.get_quantity() + qty)
                checking = True
        if not checking:
            item_obj = OrderItem(product_obj, qty)
            self.__order_list.append(item_obj)

    def get_order_details(self):
        print('----------------------------------- order data -------------------------------------')
        print(f'order id : {self.get_order_id()}')
        print(f'Customer name : {self.get_order_customer().get_name()}')
        print(f'order date : {self.get_order_date()}')
        bill_total = 0
        for item in self.__order_list:
            bill_total = bill_total + item.get_items_total()
        print('order total = ',bill_total)
        print('------------------------------------ order -----------------------------------------')
        for item in self.__order_list:
            print('Line No : ', item.get_line_no())
            print('Product Name : ', item.get_product().get_product_name())
            print('quantity : ', item.get_quantity())
            print('Unit Price : ', item.get_unit_price())
            print('Tax : ', item.get_product_tax())
            print('Total  : ', item.get_items_total())
            print('-------------------------------')
