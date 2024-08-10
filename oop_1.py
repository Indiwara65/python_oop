import datetime

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

    #class methods
    @classmethod
    def set_raise_amount(cls, amount:float):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, int(pay)) 
    
    #static methods - mehtods that require niether the class or instance
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return False
        return True




if __name__ == '__main__':
    emp_1_str = "Silvia-Nissan-200000"
    emp_2_str = "Camry-Toyota-180000"
    emp_1 = Employee.from_string(emp_1_str)
    emp_2 = Employee.from_string(emp_2_str)

    my_date = datetime.date(2024,8,12)
    print(Employee.is_workday(my_date))