from abc import abstractmethod, ABC


class Tax(ABC):
    VAT = 14
    @abstractmethod
    def get_tax(self, amount):
        pass
