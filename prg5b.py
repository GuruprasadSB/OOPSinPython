class Student:
    def __init__(self):
        self.usn = None
        self.name = None
        self.age = None

    def getdata(self):
        self.usn = input("Enter USN: ")
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

class Derived1(Student):
    def __init__(self):
        super().__init__()
        self.subjects = []

    def sub_marks(self):
        super().getdata()
        for i in range(5):
            mark = int(input(f"Enter marks for subject {i+1}: "))
            self.subjects.append(mark)

    def cal(self):
        total = sum(self.subjects)
        percentage = (total / 500) * 100
        return total, percentage

class Derived2(Derived1):
    def display(self):
        self.sub_marks()
        total, percentage = self.cal()
        print(f"USN: {self.usn}, Name: {self.name}, Age: {self.age}")
        print("Total marks:", total)
        print("Percentage:", percentage)

def main():
    n = int(input("Enter the number of students: "))
    students = []

    for i in range(n):
        print(f"Enter details for student {i + 1}:")
        s = Derived2()
        s.display()
        students.append(s)
        print()

if __name__ == "__main__":
    main()
