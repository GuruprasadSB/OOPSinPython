class Person:
    def hello(self, name=None, age=None):
        self.name = name
        self.age = age
        if self.name is not None and self.age is not None:
            if self.age.isdigit():
                print(f"Hello {self.name}, your age is {self.age}")
            else:
                print("Age should be a number.")
        elif self.name is not None:
            print(f"Hello {self.name}")
        else:
            print("Hello")

# Input and usage
name = input("Enter name: ")
age = input("Enter age: ")
p1 = Person()
p1.hello()
p1.hello(name)
p1.hello(name, age)
