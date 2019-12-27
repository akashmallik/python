class Employee:
    number_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@domain.com'

        Employee.number_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('Akash', 'Mallik', 15000)
emp_2 = Employee('Moutushy', 'Lima', 8000)


# print(emp_1.full_name())
# print(emp_2.full_name())
# print(Employee.full_name(emp_1))
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.number_of_emps)
Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)