def calculator():
    print("----------CALCULATOR----------")
    while True:
        try:
            print("Press ctrl + C to escape calculator.")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            choice = input("Choose any operation [+,-,*,/,^]: ")
            if choice == '+':
                ans = num1 + num2
            elif choice == '-':
                ans = num1 - num2
            elif choice == '*':
                ans = num1 * num2
            elif choice == '/':
                if num2 == 0:
                    print("Error: Division by zero is undefined.")
                    continue
                ans = num1 / num2
            elif choice == '^':
                if num1 == 0 and num2 == 0:
                    print("Error: Undefined calculation.")
                    continue
                ans = num1 ^ num2
            else:
                print("Invalid operation choice.")
                continue
            print(f"{num1} {choice} {num2} = {ans}")
            print("--------------------------------")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except KeyboardInterrupt:
            print("Closing Calculator")
            return

calculator()