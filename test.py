def div1(x, y):
    print("%s/%s = %s" % (x, y, x/y))


def div2(x, y):
    print("%s//%s = %s" % (x, y, x//y))


# div1(5, 2)
# div1(5., 2)
# div2(5, 2)
# div2(5., 2.)

List = ['a', 'b', 'c', 'd', 'e']
# print(list[10:])


class Base:

    def foo(self):
        print("In foo function")

    def bar(self):
        print("In bar function")


class Base2:

    def __init__(self, amount):
        self.amount = amount

    def foo(self):
        print("In foo function")

    def bar(self):
        print("In bar function")

    def char(self):
        print("Char function")


BaseAlias = Base2


class Derived(BaseAlias):

    def __init__(self, amount, name):
        super().__init__(amount)

    def some_method(self):
        super(Derived, self).bar()


class Dervied2(Derived):

    def some_other_method(self):
        super(Dervied2, self).foo()


val = Derived(23, "Vinee")
val.foo()
val.bar()

val1 = Dervied2(23, "Vinee")
val1.bar()
val1.foo()
