class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

     #methods
    def fullname(self):
        return f"{self.first} {self.last}"
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)


if __name__ == '__main__':
    emp_1 = Employee("Silvia", "Nissan", 200000)
    emp_2 = Employee("Camry", "Toyota", 180000)

    print(emp_1.fullname())
    print(Employee.fullname(emp_2))