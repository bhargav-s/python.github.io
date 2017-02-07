class Parent:
    def first_name(self):
        print("Bhargav")


class Child(Parent):
    def last_name(self):
        print("S")

    def first_name(self):
        print("SSS")

'''
override parent function
'''



c = Child()
c.first_name()
c.last_name()