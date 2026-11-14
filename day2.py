# number = int(input("Enter a number: ")) #0
# if number>=0:
#     if number == 0:
#         print("The number is zero.")
#     else:
#         print("The number is positive.")
# else:
#     print("The number is not positive.")


# num=int(input("enter a number:"))
# if num %2 == 0:
#     print("the number is even")
# elif num %2 == 1:
#     print("the number is odd")
# else:
#     print("the number is zero")

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# c=int(input("enter a number:"))
# if a > b and a > c:
#     print("a is the largest number")
# elif b > c:
#     print("b is the largest number")
# else:
#     print("c is the largest number")


# marks=int(input("enter a marks:"))
# if marks > 90:
#     print("A grade")
# elif marks < 90 and marks > 70:
#     print("B grade")
# elif marks < 70 and marks > 40:
#     print("C grade")
# else:
#     print("fail")

# day = int(input("Enter a number (1-7): "))

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid Day")

# colour=input("enter a colour(red,yellow,green):")
# match colour:
#     case "red":
#         print("stop")
#     case "yellow":
#         print("wait")
#     case "green":
#         print("gooo")
#     case _:
#         print("invalid colour")

# age=int(input("enter an age:"))
# if age >= 18:
#     print("eligible to vote")
# else:
#     print("not eligible to vote")

# units=int(input("enter a number:"))
# if units < 100:
#     print(units*2)
# elif units > 100:
#     print(units*3)
# elif units > 200:
#     print(units*5)
# else:
#     ("none of these")

# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# c=int(input("enter a number:"))
# if a+b+c == 180:
#     print("valid triangle")
# else:
#     print("not valid")

# price=int(input("enter a price:"))
# if price > 5000:
#     print((price*20)/100)
# elif price < 5000 and price > 3000:
#     print((price*10)/100)
# else:
#     print("no discount")

number=int(input("enter a number:"))
if number % 3 == 0 and number % 5 == 0:
    print("Divisible by both 3 and 5")
elif number % 3 == 0:
    print("Divisible only by 3 ")
elif number % 5 == 0:
    print("Divisible only by 5")
else:
    print("Not Divisible by either ")