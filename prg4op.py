class Op:
    def __init__(self):
        self.elements = []

    def input_elements(self):
        self.elements = [int(input("Enter value: ")) for _ in range(int(input("Enter the number of elements in the list: ")))]
        print("List: ", self.elements)

    def __add__(self, other):
        return [a + b for a, b in zip(self.elements, other.elements)]

    def __sub__(self, other):
        return [a - b for a, b in zip(self.elements, other.elements)]

    def __mul__(self, other):
        return [a * b for a, b in zip(self.elements, other.elements)]

    def __floordiv__(self, other):
        return [a // b for a, b in zip(self.elements, other.elements)]
