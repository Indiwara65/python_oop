class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"


if __name__ == '__main__':
    emp_1 = Employee("Silvia", "Nissan", 200000)
    emp_2 = Employee("Camry", "Toyota", 180000)

    print(emp_1.email)
    print(emp_2.email)