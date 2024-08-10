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



if __name__ == '__main__':
    print(Employee.num_of_emps)
    emp_1 = Employee("Silvia", "Nissan", 200000)
    print(Employee.num_of_emps)
    emp_2 = Employee("Camry", "Toyota", 180000)
    print(Employee.num_of_emps,'\n')

    print(Employee.raise_amount)
    emp_1.raise_amount = 1.05
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    #
    print('\n')
    #
    Employee.raise_amount = 1.045
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)