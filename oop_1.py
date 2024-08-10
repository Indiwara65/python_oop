class Employee:
    #class variables
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

     #methods
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)  # or self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount:float):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay)) 



if __name__ == '__main__':
    emp_1_str = "Silvia-Nissan-200000"
    emp_2_str = "Camry-Toyota-180000"
    emp_1 = Employee.from_string(emp_1_str)
    emp_2 = Employee.from_string(emp_2_str)

    print(emp_1.email)
    print(emp_2.email)
    print("\n")
    #
    Employee.set_raise_amount(1.06)
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)