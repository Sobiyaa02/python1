balance=10000
for i in range(5):
    print("Click 1 for Check Balance:")
    print("Click 2 for Deposite Money:")
    print("Click 3 for Withdraw Money:")
    print("Click 4 for Exit:")
    choice=int(input("enter a number:"))
    if choice == 1:
        print("Your balance is:",balance)
        break
    elif choice == 2:
        Depositeamount=int(input("enter a deposite amount:"))
        if Depositeamount > 0:
            print("Your deposite amount is:",Depositeamount)
            balance=Depositeamount+balance
            print("your final balance is:",balance)
        else:
            print("please enter correct amount")
        break
    elif choice == 3:
        Withdraw=int(input("enter a  withdraw amount:"))
        if Withdraw <= 0:
            print("enter valid amount")
        elif Withdraw > balance:
            print("insufficient balance")
        else:
            print("Your withdraw amount is:",Withdraw)
            balance=balance-Withdraw
            print("your final balance is:",balance)
        break
    elif choice == 4:
        print("thank you for visiting")
        break
    else:
        print("please enter a valid choice")