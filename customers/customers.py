class Customer:
    def __init__(self, _id, name, phone, address):
        self.__customer_id = _id
        self.__customer_name = name
        self.__customer_phone = phone
        self.__customer_address = address

    def get_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__customer_name

    def get_phone(self):
        return self.__customer_phone

    def get_address(self):
        return self.__customer_address

    def set_id(self, customer_id):
        self.__customer_id = customer_id

    def set_name(self, name):
        self.__customer_name = name

    def set_phone(self, phone):
        self.__customer_phone = phone

    def set_address(self, address):
        self.__customer_address = address



