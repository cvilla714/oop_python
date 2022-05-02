class Person:
    def __init__(self, name):
        self.name = name
        self._salary = 0
# using new way to add property
    @property
    def salary(self):
        return round(self._salary)

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError('Invalid salary')
        self._salary = value

    # def set_salary(self, salary):
    #     if  salary < 0:
    #         raise ValueError("Salary cannot be negative")
    #     self._salary = salary
    #
    # def get_salary(self):
    #     return round(self._salary)

    # salary = property(get_salary, set_salary)

p = Person('Bob')
p.salary = 103.7750
# p.salary = -103.7750
print(p.salary)
# p.set_salary(103)
# print(p.set_salary)


class Time:
    def __init__(self, second):
        self._second = second

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        if second < 0 or second > 60:
            raise ValueError('Invalid!')
        self._second = second

t = Time(54)
t.second= -58
print(t.second)



