# for i in range(1,21):
#     if i % 2 == 0:
#         print(i,"even number")
#     else:
#         print(i,"odd number")

# num=int(input("enter a number:"))
# for i in range(1,11):
#     print(num,"x",i,"=",num*i)
#     if (num*i) % 2 ==0:
#         print("even")
#     else:
#         print("odd")

# Pass=0
# Fail=0
# for i in range(5):
#     num=int(input("enter a number:"))
#     if num >= 35:
#         Pass += 1 
#     else:
#         Fail += 1
# print("Total Pass:",Pass)
# print("Total Fail:",Fail)
   
for i in range(1,51):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"Fizz Buzz")
    elif i % 3 == 0:
        print(i,"Fizz")
    elif i % 5 == 0:
        print(i,"Buzz")
    else:
        print(i)
    