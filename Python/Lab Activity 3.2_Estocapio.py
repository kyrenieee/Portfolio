name = input("Enter your name: ")
age =  int (input("Enter your age: "))
time_slot = (input("What will you watch? "))

#ticket prices
daytime_ticket1 = 50
daytime_ticket2 = 100
daytime_ticket3 = 80
evening_ticket1 = 70
evening_ticket2 = 120
evening_ticket3 = 100

match time_slot: 
    case "daytime":
        print ("You will be watching a daytime show!")
    case "evening":
        print ("You will be watching an evening show!")
    case "_":
        print ("There seems to be an error with your input.")
        
if 0 <= age <= 4:
    print("You can watch for free!")
elif 5 <= age <= 17:
    if time_slot == "daytime":
        print("That will be: PHP", daytime_ticket1)
        print("Please proceed.")
        price = daytime_ticket1
    elif time_slot == "evening":
        print("That will be: PHP", evening_ticket1)
        print("Please proceed.")
        price = evening_ticket1
elif 18 <= age <= 64:
    if time_slot == "daytime":
        print("That will be: PHP", daytime_ticket2)
        print("Please proceed.")
        price = daytime_ticket2
    elif time_slot == "evening":
        print("That will be: PHP", evening_ticket2)
        print("Please proceed.")
        price = evening_ticket2
elif age <= 65:
    if time_slot == "daytime":
        print("That will be: PHP", daytime_ticket3)
        print("Please proceed.")
        price = daytime_ticket3
    elif time_slot == "evening":
        print("That will be: PHP", evening_ticket3)
        print("Please proceed.")
        price = evening_ticket3
else:
    print("There seems to be an error with your input.")

verification = (input("Will you proceed with your ticket?: "))
if verification == "yes":
    print("* * * * * * * * * * * * * * * * * * * * * *")
    print("Name:", name)
    print("Age: ", age)
    print("Time: ", time_slot)
    print("Price: PHP",price)
    print("Thank you for purchasing a ticket!")
    print("* * * * * * * * * * * * * * * * * * * * * *")
elif verification == "no":
    print("Thank you for your time.")
else:
    print("There seems to be a problem with your transaction.")




