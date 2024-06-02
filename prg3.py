class Employee:
    def __init__(self):
        self.employees = {}

    def add_employee(self):
        n = int(input("Enter number of employees: "))
        for i in range(1, n + 1):
            temp = dict()
            empno = input("Enter empno: ")
            temp["name"] = input("Enter a Name: ")
            temp["address"] = input("Enter an Address: ")
            temp["pan"] = input("Enter a PAN: ")
            temp["basic"] = int(input("Enter Basic: "))
            temp["tds"] = int(input("Enter TDS: "))
            temp["deduct"] = int(input("Enter Deduct: "))
            temp["hra"] = int(input("Enter HRA: "))
            temp["da"] = int(input("Enter DA: "))
            temp["salary"] = self.cal_salary(temp)
            self.employees[empno] = temp

    def update_employee(self):
        empno = input("Enter employee ID: ")
        if empno in self.employees:
            print("Update Employee Details:")
            employee = self.employees[empno]
            for key in employee.keys():
                if key != "empno":
                    if key == "salary":
                        continue
                    new_value = input(f"Enter new {key} (Press enter to keep the same): ")
                    if new_value:
                        if key in ["basic", "tds", "deduct", "hra", "da"]:
                            employee[key] = int(new_value)
                        else:
                            employee[key] = new_value
            employee["salary"] = self.cal_salary(employee)
            print("Employee details updated successfully.")
        else:
            print(f"Employee with ID {empno} not found.")

    def clear_employee(self):
        empno = input("Enter employee ID: ")
        if empno in self.employees:
            del self.employees[empno]
            print(f"Employee with the ID {empno} deleted.")
        else:
            print(f"Employee with the ID {empno} not found.")

    def cal_salary(self, employee):
        basic = employee["basic"]
        hra = employee["hra"]
        da = employee["da"]
        deduct = employee["deduct"]
        tds = employee["tds"]
        salary = basic + hra + da - deduct - tds
        return salary

    def display_employees(self):
        for empno, employee in self.employees.items():
            print("Employee ID: ", empno)
            for key, value in employee.items():
                print(f"{key}: {value}")

    def display_an_employee(self):
        empno = input("Enter employee ID: ")
        if empno in self.employees:
            employee = self.employees[empno]
            print("Employee ID: ", empno)
            for key, value in employee.items():
                print(f"{key}: {value}")
        else:
            print(f"Employee with ID {empno} not found.")


emp1 = Employee()

while True:
    print("1: Add\n2: Display all employees\n3: Display an employee\n4: Delete Employee\n5: Update Employee\n6: Exit")

    op = int(input("Enter your choice: "))

    if op == 1:
        emp1.add_employee()
    elif op == 2:
        emp1.display_employees()
    elif op == 3:
        emp1.display_an_employee()
    elif op == 4:
        emp1.clear_employee()
    elif op == 5:
        emp1.update_employee()
    elif op == 6:
        break
    else:
        print("Invalid input")
