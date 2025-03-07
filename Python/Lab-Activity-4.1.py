machine = ["Check Balance", "Withdraw Money", "Deposit Money", "Exit Application"]
transaction = True

print('''Welcome to the app of Infinite Money Bank
Please type in the command of your chosen transaction below [1-4]''')
print ("=====" * 10)
while transaction:
    balance = 100.00
    num = 0
    for transaction in machine:
        print(f"[{num + 1}]{machine[num]}")
        num = num + 1
    print ("=====" * 10)

    command = (input("Please enter you command: "))

    if command == "1":
        print("Your current balance is: PHP", balance)
    elif command == "2":
        withdraw = int(input("Please enter the amount you would like to withdraw: "))
        print("You have withdrawn an amount of PHP", withdraw)
        if withdraw > balance:
            print("You cannot withdraw the given amount")
        else:
            balance <= withdraw
            print("You have withdrawn an amount of PHP", withdraw)
            print("Your current balance is: PHP", (balance - withdraw))
    elif command == "3":
        deposit = int (input("Please enter the amount you would like to deposit: "))
        print("You have deposited and amount of: PHP", deposit)
        print("Your current balance is: PHP ", (balance + deposit))
    elif command == "4":
        print("Thank you for using our app. Have a nice day!")
        break
    else:
        print("There seems to be a problem with your command. Please choose a command from 1 - 4.")

