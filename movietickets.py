walletbalance=5000
for i in range(5):
    print("click 1 for walletbalance:")
    print("click 2 for  booktickets")
    print("click 3 for addmoney")
    print("click 4 for exit")
    choice=int(input("enter your choice:"))
    if choice == 1:
        print("your current balance:",walletbalance)
    elif choice==2:
        print("Available tickets")
        print("1.leo")
        print("2.goat")
        print("3.beast")
        print("4.thupakki")
        selected_movies=int(input("enter your movie choice"))
        if selected_movies == 1:
            movie_name = "leo"
            price = 200
        elif selected_movies == 2:
            movie_name = "goat"
            price = 150 
        elif selected_movies == 3:
            movie_name = "beast"
            price = 250
        elif selected_movies == 4:
            movie_name = "thupakki"
            price = 200
        else:
            print("invalid movie")
        quantity = int(input("no.of.tickets:"))
        if quantity <= 0:
            print("please enter atleast one ticket")
        else:
            total=price*quantity
            print("movie_name",movie_name)
            print("no.of.tickets selected:",quantity)
            print("totalamount:",total)
            if walletbalance >= total:
                print("ticket booked successfully!!")
                walletbalance=walletbalance-total
                print("walletbalance",walletbalance)
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
        print("thank you for booking")
    else:
        print("invalid operation")





        
        
    

        
        