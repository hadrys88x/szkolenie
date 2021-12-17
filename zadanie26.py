class Employee:
    OVERTIME_MULTIPLIER = 2;

    def __init__(self, name: str, surname: str, salary: int, overtime = 0, normal_time = 0):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.overtime = overtime
        self.normal_time = normal_time

    def register_time(self, current_time: int):
        pre_over_time = current_time - 8
        if (pre_over_time > 0):
            self.overtime = self.overtime + pre_over_time
        else:
            pre_over_time = 0
        self.normal_time = self.normal_time + current_time - pre_over_time

    def pay_sallary(self):
        return (self.normal_time * self.salary) + ((self.overtime * self.salary) * Employee.OVERTIME_MULTIPLIER)

    def clear(self):
        self.normal_time = 0
        self.overtime = 0

employee = Employee("Jan", "Kowalski", 100)
employee.register_time(10)
employee.register_time(9)
employee.register_time(1)
print(employee.pay_sallary())
employee.clear()
print(employee.pay_sallary())