class Animal:
    def walk(self):
        pass

    def communicate(self):
        pass

class Cat(Animal):
    def walk(self):
        print("Cat is walking")

    def communicate(self):
        print("Meow")

class Dog(Animal):
    def walk(self):
        print("Dog is walking")

    def communicate(self):
        print("Bark")

def main():
    cat = Cat()
    dog = Dog()

    cat.walk()
    cat.communicate()

    dog.walk()
    dog.communicate()

if __name__ == "__main__":
    main()
