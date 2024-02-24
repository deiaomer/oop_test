from customers.customers import Customer

class Company(Customer):
    def __init__(self, _id, name, phone, address, company_contact, company_discount):
        super().__init__(_id, name, phone, address)
        self.__company_contact = company_contact
        self.__company_discount = company_discount

    def get_company_contact(self):
        return self.__company_contact

    def set_company_contact(self, company_contact):
        self.__company_contact = company_contact

    def get_company_discount(self):
        return self.__company_discount

    def set_company_discount(self, company_discount):
        self.__company_discount = company_discount





