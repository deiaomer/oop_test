from customers.company import Company
from order.order import Order
from order_item.order_items import OrderItem
from products.hardware import Hardware
from products.software import Software

keyboard = Hardware(101, 'keyboard', 100, 'accessories', 1)
office2022 = Software(102, 'office2022', 150, 'MSoffice', '1254-5847-1542')
printer = Hardware(103,'canon printer', 500, 'laser jet', 1)
raya = Company(1, 'raya_company', '0152031548', 'cairo', 'mr.khalid', 0)
my_order = Order(raya, 40)
my_order.add_to_cart(keyboard, 1)
my_order.add_to_cart(keyboard, 3)
my_order.add_to_cart(office2022, 2)

my_order.get_order_details()






