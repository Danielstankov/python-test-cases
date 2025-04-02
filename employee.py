class Employee:

    raise_amount_percent = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay


    def fullname(self):
        return f"{self.first} {self.last}"


    def email(self):
        return f"{self.first}.{self.last}@email.com"


    def apply_raise(self):
        self.pay = self.pay * self.raise_amount_percent