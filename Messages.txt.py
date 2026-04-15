
try:
    file = open(filename, "x")
    file.close()
except FileExistsError:
    print("File already exists")

while True:
    print("\nWelcome to Messaging App")
    print("1. Send Message")
    print("2. View Messages")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = input("Enter your message: ")

        with open(filename, "a") as file:
            file.write(message + "\n")

        print("Message sent!")

    elif choice == "2":
        print("\n--- Messages ---")
        try:
            with open(filename, "r") as file:
                content = file.read()
                if content:
                    print(content)
                else:
                    print("No messages yet.")
        except FileNotFoundError:
            print("No messages found.")

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")