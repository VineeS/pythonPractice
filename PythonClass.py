import datetime


class employee:
    # initalize the class or can be a constructor
    name = ''
    raise_amount = 1

    def __init__(self, firstname, lastname, salary):
        # above takes the class instance which is called as self
        self.firstname = firstname  # self refers to current instance of a python class
        self.lastname = lastname
        self.salary = salary

        self.email = self.firstname + "." + self.lastname + "@kite.com"
        # class variables are initialized with self.variablename

    def give_raise(self, salary):
        self.salary = salary
        print("Name Please", self.firstname)

    def full_name(self):  # regular method
        return '{} {}'.format(self.firstname, self.lastname)

    def amout_bonus(self):
        total_value = int(self.salary + self.raise_amount)
        return total_value

    @classmethod
    def increment_the_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, empoyee_string):
        firstname, lastname, pay = empoyee_string.split('-')
        return cls(firstname, lastname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

    def __repr__(self):
        return "employee('{}', '{}' ,'{}')".format(self.firstname, self.lastname, self.salary)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    def __add__(self, other):
        return self.salary + other.salary


# these are the instances of the class employee
employee1 = employee("Vinee", "Shukla", 2000)
employee2 = employee("Aman", "Sharma", 3000)
print("--> ", employee1.email)
print("***********")
print(employee1)
print("***********")
# print(employee1)  # employee class instance
# print(employee2)
# Object is a copy of the class. Instance is a variable that
# holds the memory address of the object. You can also have multiple objects of
# the same class and then multiple instances of each of those objects.
# In these cases, each object's set of instances are equivalent
# in value, but the instances between objects are not
# print(employee1.email)
# employee1.giveRaise(20)
# employee1.fullName()

# topic 1 : Class variable and instance variable
print(employee1.raise_amount)
employee2.raise_amount = 2
print(employee2.raise_amount)
print(employee.raise_amount)

# topic 2: Regular method , static method, class methods

# class method
emp_string_one = 'Jane-Doe-2000'
emp_string_two = 'John-Doe-4000'

first = employee.from_string(emp_string_one)
print(first.email)
print(first.firstname)
print(first.lastname)
print(first.salary)

second = employee.from_string(emp_string_two)
print(second.email)
print(second.firstname)
print(second.lastname)
print(second.salary)


# static method
my_date = datetime.date(2021, 7, 31)
print(employee.is_workday(my_date))

# topic 3: Inheritance


# class Developer(employee):
# pass
#

# dev1 = Developer("Aman", "Sharma", 170000)
# print(dir(dev1))

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'amout_bonus', 'email', 'firstname', 'from_string', 'full_name', 'give_raise',
# 'increment_the_raise_amount', 'is_workday', 'lastname', 'name', 'raise_amount', 'salary']

# print(dev1.__dict__)

#  ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
#   '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
#   '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
#   '__str__', '__subclasshook__', '__weakref__', 'amout_bonus', 'email', 'firstname',
#   'from_string', 'full_name', 'give_raise', 'increment_the_raise_amount', 'is_workday',
#   'lastname', 'name', 'raise_amount', 'salary']
# {'firstname': 'Aman', 'lastname': 'Sharma', 'salary': 170000, 'email': 'Aman.Sharma@kite.com'}

# print(help(dev1))  # you can see the method resolution order


class Developer(employee):
    raise_amount = 1.05

    def __init__(self, firstname, lastname, salary, programming_language):
        super().__init__(firstname, lastname, salary)
        self.programming_language = programming_language


dev1 = Developer("Vinee", "shukla", 40000, 'python')
dev2 = Developer("Aman", "sharma", 40000, 'java')
print(dev1.email)
print(dev1.amout_bonus())
dev1.raise_amount = 100
print(dev1.raise_amount)
print(dev1.amout_bonus())


print(dev2.email)


class Manager(employee):
    def __init__(self, firstname, lastname, salary, employees_under=None):
        super().__init__(firstname, lastname, salary)
        if employees_under is None:
            self.employees_under = []
        else:
            self.employees_under = employees_under

    def add_employees(self, employees_to_be_added):
        if employees_to_be_added not in self.employees_under:
            self.employees_under.append(employees_to_be_added)

    def delete_employee(self, employees_to_be_deleted):
        if employees_to_be_deleted in self.employees_under:
            self.employees_under.remove(employees_to_be_deleted)

    def show_all_employees(self):
        for emp in self.employees_under:
            print("-->", emp.email)

    def __len__(self):
        return len(self.employees_under)


man1 = Manager("Smith", "Cloud", 300000, [dev1, dev2])
man1.full_name()
print("---> ", man1.email)
print("........ Employees of Smith.......")
man1.show_all_employees()

man1.delete_employee(dev1)
print("........ Deletion Employees of Smith.......")
man1.show_all_employees()

man1.add_employees(dev1)
print("........ adding Employees of Smith.......")
man1.show_all_employees()


######### Topic 5 Magic or Dunder methods #########
#repr and str
print(repr(employee1))
print(str(employee1))

print(employee1.__repr__())
print(employee1.__str__())
print(int.__add__(1, 2))
print(str.__add__('1', '2'))
# by using __add__ as a method in class it will add the salary
print(employee1+employee2)

print(len(man1))
