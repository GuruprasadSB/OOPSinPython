from prg4op import Op

def main():
    obj1 = Op()
    obj2 = Op()

    obj1.input_elements()
    obj2.input_elements()

    operations = {
        1: ("Addition", lambda: obj1 + obj2),
        2: ("Subtraction", lambda: obj1 - obj2),
        3: ("Multiplication", lambda: obj1 * obj2),
        4: ("Floor division", lambda: obj1 // obj2),
    }

    while True:
        print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Floor division\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice in operations:
            op_name, operation = operations[choice]
            result = operation()
            print(f"{op_name} of lists = {result}")
        elif choice == 5:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
