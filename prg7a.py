class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, empid, pay):
        self.first = first
        self.last = last
        self.empid = empid
        self.pay = pay

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def display_details(self):
        print(f"First name of employee: {self.first}")
        print(f"Last name: {self.last}")
        print(f"Employee ID: {self.empid}")
        print(f"Pay of employee: {self.pay}")

class Developer(Employee):
    raise_amt = 1.05

class Manager(Employee):
    raise_amt = 1.06

def main():
    while True:
        print("1. Developer\n2. Manager\n3. Exit")
        ch = int(input("Enter your choice between 1, 2, and 3, where 3 means exit: "))
        
        if ch == 1:
            dev_count = int(input("Enter number of developers: "))
            for _ in range(dev_count):
                first = input("Enter first name of the developer: ")
                last = input("Enter last name of the developer: ")
                empid = input("Enter empid of the developer: ")
                pay = float(input("Enter pay of the developer: "))
                emp = Developer(first, last, empid, pay)
                emp.apply_raise()
                emp.display_details()
        
        elif ch == 2:
            man_count = int(input("Enter number of managers: "))
            for _ in range(man_count):
                first = input("Enter first name of the manager: ")
                last = input("Enter last name of the manager: ")
                empid = input("Enter empid of the manager: ")
                pay = float(input("Enter pay of the manager: "))
                emp = Manager(first, last, empid, pay)
                emp.apply_raise()
                emp.display_details()
        
        elif ch == 3:
            break
        
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()
