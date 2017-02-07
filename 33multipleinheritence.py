class Parent:
    def function1(self):
        print('This is class 1')

class Child1:
    def function2(self):
        print('This is class 2')

class Child2(Parent,Child1):
    pass

c = Child2()
c.function1()
c.function2()