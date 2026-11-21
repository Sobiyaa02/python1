walletbalance=3000
for i in range(5):
    print("click 1 for wallent balance")
    print("click 2 for orderfoods")
    print("click 3 for addmoney")
    print("click 4 for exit")
    choice=int(input("enter your choice:"))
    if choice == 1:
        print("your balance is",walletbalance)
    elif choice == 2:
        print("Available Foods")
        print("Burger")
        print("Pizza")
        print("pasta")
        print("friedrice")
        print("noodles")
        selected_food=int(input("select yoyr food:"))
        if selected_food == 1:
            food = "burger"
            price = 150
        elif selected_food == 2:
            food = "pizza"
            price = 200
        elif selected_food == 2:
            food = "pizza"
            price = 200
        elif selected_food == 3:
            food = "pasta"
            price = 180
        elif selected_food == 4:
            food = "friedrice"
            price = 120
        elif selected_food == 2:
            food = "noodles"
            price = 140
        else:
            print("invalid food")
        quantity=int(input("quantity of food:"))
        if quantity <= 0:
            print("please order atleast one food")
        else:
            total=price*quantity
            print("food",food)
            print("quantity of foods:",quantity)
            print("totalamount:",total)
            if walletbalance >= total:
                print("your food ordered successfully!!")
                walletbalance=walletbalance-total
                print("remaing_balance",walletbalance)
            else:
                print("insufficient balance")
    elif choice == 3:
            addmoney=int(input("enter your amount:"))
            if addmoney >= 0:
                walletbalance=walletbalance+addmoney
                print("money added successfully")
                print("walletbalance:",walletbalance)
            else:
                print("please enter a valid amount")
    elif choice == 4:
            print("thank you for visitingggg!!!")
            break
    else:
            print("invalid operation")