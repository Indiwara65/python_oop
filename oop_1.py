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
    emp_1 = Employee("Creseda", "Toyota", 160000)
    emp_2 = Employee("Covette", "Chevy", 170000)
    #
    dev_1 = Developer("Silvia", "Nissan", 200000, "Python")
    dev_2 = Developer("Camry", "Toyota", 180000, "Java")
    #
    emp_man = Manager("Patrol", "Nissan", 4250000, [emp_1, emp_2])
    dev_man = Manager("Cruiser", "Toyota", 450000, [dev_1, dev_2])

    
    print(emp_1.email)
    print(emp_2.email)
    print('\n')
    #
    print(dev_1.email)
    print(dev_2.email)
    print('\n')
    #
    print(dev_1.prog_lang)
    print(dev_2.prog_lang)
    print("\n")
    #
    print(f"{emp_man.fullname()}:")
    Manager.print_emps(emp_man)
    print("\n")
    print(f"{dev_man.fullname()}: ")
    Manager.print_emps(dev_man)

    #
    print("\n")
    print(isinstance(emp_man, Manager))
    print(issubclass(Employee, Manager))