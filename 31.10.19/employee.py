class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name



class HourlyEmployee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def weekly_pay(self, hours):
        if(hours > 40):
            pay = self.salary * 40
            hours -= 40

            pay += (1.5 * self.salary) * hours
            return pay

        return self.salary * hours



class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)

    def weekly_pay(self, hours):
        return (self.salary/52)



class Manager(SalariedEmployee):
    def __init__(self, name, salary, weekly_bonus):
        Employee.__init__(self, name, salary)
        self.bonus = weekly_bonus
    
    def weekly_pay(self, hours):
        pay = SalariedEmployee.weekly_pay(self, hours)
        pay += self.bonus
        return pay



emp3 = Manager("Mary Smith", 91000.0, 60.0)
pay = emp3.weekly_pay(60)
print(pay)