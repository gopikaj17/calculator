def calculator():
    print("\t____CALCULATOR____")

    while True:
        print("\n\nChoose the operation you want to perform: ")
        print("\n\t1.ADDITION")
        print("\n\t2.SUBTRACTION")
        print("\n\t3.MULTIPLICATION")
        print("\n\t4.DIVISION")
        print("\n\t5.EXIT")

        choice = int(input('>'))

        if choice == 5:
            print("\nChose to exit")
            break

        if choice not in range(1, 5):
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        print("\n\nEnter the two numbers: ")
        num1 = int(input('>'))
        num2 = int(input('>'))

        if choice == 1:
            result = num1 + num2
            print(f"The sum is : {result}")

        elif choice == 2:
            result = abs(num1 - num2)
            print(f"The difference is : {result}")

        elif choice == 3:
            result = num1 * num2
            print(f"The product is : {result}")

        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"The divided value is : {result}")
            else:
                print("Cannot divide by zero. Please enter a non-zero divisor.")
                continue

calculator()
