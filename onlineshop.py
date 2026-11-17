balance=20000
for i in range(5):
    print("Click 1 for Wallet Balance:")
    print("Click 2 for product purchase:")
    print("Click 3 for add money:")
    print("Click 4 for exit:")
    choice=int(input("enter a choice:"))
    if choice == 1:
        print("your balance is:",balance)
    elif choice ==2:
        productprice=int(input("enter a amount:"))
        if productprice < 0:
            print("enter a valid amount:")
        elif productprice > balance:
            print("insufficient balance")
        else:
            print("your productprice is",productprice)
            balance=balance-productprice
            print("your remaining balance:",balance)
    elif choice == 3:
        addmoney=int(input("enter a amount"))
        if addmoney > 0:
            print("your addmoney is",addmoney)
            balance=balance+addmoney
            print("your money is added:",balance)
        else:
            print("enter valid amount")
    elif choice==4:
        print("thanks for coming")
        break
    else:
        print("your choice is invalid")
            


