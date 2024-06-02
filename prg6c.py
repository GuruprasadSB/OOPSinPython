class Overload:
    def load(self, a=None, b=None):
        if a is not None and b is not None:
            if a.isalpha() and b.isalpha():
                print("Concatenate:", a + b)
            elif a.isdigit() and b.isdigit():
                print("Sum:", int(a) + int(b))
            else:
                print("Both parameters should be either strings or numbers.")
        else:
            print("Both parameters are required.")

# Input and usage
s1 = input("Enter a string1: ")
s2 = input("Enter a string2: ")
int1 = input("Enter first number: ")
int2 = input("Enter second number: ")

over = Overload()
over.load(s1, s2)
over.load(int1, int2)
