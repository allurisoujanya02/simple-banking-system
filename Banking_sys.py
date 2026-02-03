# Simple Banking System

# Initial balance
balance = 1000  # Starting balance for the user

# Welcome message
print("Welcome to the Simple Banking System!")

# Infinite loop to keep the program running until user exits
while True:
    # Show menu options
    print("\nPlease select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    # Take user input
    choice = input("Enter your choice (1-4): ")

    # Option 1: Check Balance
    if choice == "1":
        print("Your current balance is: $", balance)

    # Option 2: Deposit Money
    elif choice == "2":
        deposit = input("Enter amount to deposit: $")

        # Check if input is a valid number
        if deposit.isdigit():
            deposit = int(deposit)
            balance += deposit
            print(f"${deposit} deposited successfully. New balance: ${balance}")
        else:
            print("Invalid amount! Please enter a number.")

    # Option 3: Withdraw Money
    elif choice == "3":
        withdraw = input("Enter amount to withdraw: $")

        # Check if input is a valid number
        if withdraw.isdigit():
            withdraw = int(withdraw)

            if withdraw <= balance:
                balance -= withdraw
                print(f"${withdraw} withdrawn successfully. New balance: ${balance}")
            else:
                print("Insufficient balance!")
        else:
            print("Invalid amount! Please enter a number.")

    # Option 4: Exit
    elif choice == "4":
        print("Thank you for using the Simple Banking System. Goodbye!")
        break  # Exit the loop and end program

    # Invalid choice
    else:
        print("Invalid choice! Please select a valid option (1-4).")
