balance = 5000 

while True:
    print("\n--- ATM MENU ---")
    print("1. Withdraw Money")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    try:
        if choice == "1":
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
                continue

            elif amount > balance:
                print("Insufficient balance.")
                print("1. Re-enter Amount")
                print("2. Check Balance")
                print("3. Exit")

                option = input("Choose your option (1-3): ")

                if option == "1":
                    continue
                elif option == "2":
                    print(f"Current balance: {balance}")
                    continue
                elif option == "3":
                    print("Exiting program...")
                    break
                else:
                    print("Invalid option.")
                    continue

            else:
                balance -= amount
                print(f"Withdrawal successful! New balance: {balance}")

        elif choice == "2":
            print(f"Current balance: {balance}")

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please select 1-3.")

    except ValueError:
        print("\nError: Invalid input. Please enter numbers only.")
        print("1. Re-enter Amount")
        print("2. Check Balance")
        print("3. Exit")

        option = input("Choose your option (1-3): ")

        if option == "1":
            continue
        elif option == "2":
            print(f"Current balance: {balance}")
            continue
        elif option == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid option.")
            continue
    finally:
        print("Executed")        