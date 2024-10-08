
class Employee:
    #class variables
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

     #methods
    
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
    
    #special methods
    def __repr__(self) -> str:
        return f"Employee({self.first}, {self.last}, {self.pay})"
    
    def __str__(self) -> str:
        return f"{self.first} - {self.last} - {self.email}"
    
    def __add__(self, other) ->int:
        return self.pay + other.pay
    
    def __len__(self) ->str:
        return len(self.fullname())
    

    #with property decorator a method can be called as a attribute
    @property
    def email(self):
        return f"{(self.first.lower())}.{self.last.lower()}@company.com"
    
    @property
    def fullname(self):
        return f"{self.first} {self.last}"
    
    #but using a setter a mehtod can be defined to set instance varaibles
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    #deleter
    @fullname.deleter
    def fullname(self):
        self.first = None
        self.last = None

class Developer(Employee):
    raise_amount = 1.2

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
    
    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    
    def print_emps(self):
        for employee in self.employees:
            print(employee.fullname())


if __name__ == '__main__':
    emp = Employee("Creseda", "Toyota", 160000)
    #original
    print(emp.fullname)
    #setter
    emp.fullname = "Cresta Toyota"
    print(emp.fullname)
    #delter
    del emp.fullname
    print(emp.fullname)