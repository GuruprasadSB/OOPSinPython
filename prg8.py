while True:
    print("1. Value Error\n2. File not found error\n3. Type Error\n4. IO Error\n5. Name Error\n6. Exit")
    n = int(input("Enter your choice: "))

    if n == 1:
        try:
            f = open('f1.txt', 'z')
            print("Successful")
        except ValueError:
            print("Value Error")
        print()

    elif n == 2:
        try:
            f = open('f1.txt', 'r')
            print("Successful")
        except FileNotFoundError:
            print("File not found error")

    elif n == 3:
        try:
            f = open('f1.txt', 'r', 'w')  # This line will raise a TypeError
            print("Successful")
        except TypeError:
            print("Type Error")

    elif n == 4:
        try:
            f = open('f1.txt', 'w+')
            f.write('sample')
            f1 = open('f2.txt', 'r')  # This line will raise an IOError
            print("Successful")
        except IOError:
            print("IO Error")

    elif n == 5:
        try:
            f = open('f1.txt', 'r')  # This line will raise a NameError
            print("Successful")
        except NameError:
            print("Name Error")

    elif n == 6:
        break
    else:
        print("Wrong input")
        break
