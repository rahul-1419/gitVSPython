class Employee:
    def __init__(self,name,id,dep,salary):
        self.name = name
        self.id = id
        self.dep = dep
        self.salary = salary

    def check_info(self):
        print(f"Employee Name {self.name} his Id is {self.id}. His Department is {self.dep} & his Salary is {self.salary}")

emp_info = Employee("Rahul",200490111005,'EC',10)

emp_info.check_info()