class Student:
    def __init__(self):
        self.usn = input("Enter USN: ")
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def display(self):
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Age:", self.age)

class UGStudent(Student):
    def __init__(self):
        super().__init__()
        self.sem = input("Enter semester: ")
        self.fees = int(input("Enter fees: "))
        self.stipend = int(input("Enter stipend: "))
        self.display()

    def display(self):
        super().display()
        print("Semester:", self.sem)
        print("Fees:", self.fees)
        print("Stipend:", self.stipend)

class PGStudent(Student):
    def __init__(self):
        super().__init__()
        self.sem = input("Enter semester: ")
        self.fees = int(input("Enter fees: "))
        self.stipend = int(input("Enter stipend: "))
        self.display()

    def display(self):
        super().display()
        print("Semester:", self.sem)
        print("Fees:", self.fees)
        print("Stipend:", self.stipend)

def main():
    while True:
        print("1. UG\n2. PG\n3. Exit")
        ch = int(input("Enter choice: "))
        if ch == 1:
            UGStudent()
        elif ch == 2:
            PGStudent()
        elif ch == 3:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
