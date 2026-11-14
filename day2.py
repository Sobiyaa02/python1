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


marks=int(input("enter a marks:"))
if marks > 90:
    print("A grade")
elif marks < 90 and marks > 70:
    print("B grade")
elif marks < 70 and marks > 40:
    print("C grade")
else:
    print("fail")