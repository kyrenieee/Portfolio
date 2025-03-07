
machine = ["Check Balance", "Withdraw Money", "Deposit Money", "Exit Application"]
transaction = True
balance = 100.00

print('''Welcome to the app of Infinite Money Bank
Please type in the command of your chosen transaction below [1-4]''')
print ("====" * 10)
while transaction:
    num = 0
    for transaction in machine:
        print(f"[{num + 1}]{machine[num]}")
        num = num + 1
    print ("====" * 10)

    command = (input("Please enter you command: "))

    if command == "1":
            print("Your current balance is: PHP", balance)
            print ("====" * 10)
    elif command == "2":
            while True:
                withdraw = int(input("Please enter the amount you would like to withdraw: PHP "))
                if withdraw > balance:
                    print("Insufficient amount.")
                elif withdraw <= balance and withdraw > 0:
                    balance = balance - withdraw
                    print("You have withdrawn an amount of PHP", withdraw)
                    print("Your current balance is: PHP", balance)
                    break
                else:
                    print("You cannot withdraw the given amount.")
            print ("====" * 10)
    elif command == "3":
        while True:
            deposit = int (input("Please enter the amount you would like to deposit: PHP "))
            if deposit < 0:
                print("Please enter a positive amount.")
            elif deposit <= balance:
                print("You cannot deposit the given amount.")
            else:
                balance = balance + deposit
                print("You have deposited and amount of: PHP", deposit)
                print("Your current balance is: PHP ", balance)
                break
        print ("====" * 10)
    elif command == "4":
        print("Thank you for using our app. Have a nice day!")
        break
    else:
        print("There seems to be a problem with your command. Please choose acommand from 1 - 4.")
