from customers.customers import Customer


class Individual(Customer):
    def __init__(self, _id, name, phone, address, lic_no):
        super().__init__(_id, name, phone, address)
        self.__individual_lic_no = lic_no

    def get_individual_lic_no(self):
        return self.__individual_lic_no

    def set_individual_lic_no(self,lic_no):
        self.__individual_lic_no = lic_no

        