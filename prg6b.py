class Number:
    def area(self, n1=None, n2=None):
        if n1 is not None and n2 is not None:
            print("Area of Rectangle:", n1 * n2)
        elif n1 is not None:
            print("Area of Square:", n1 * n1)
        else:
            print("Area: 0")

# Input and usage
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
a = Number()
a.area()
a.area(length)
a.area(length, breadth)
