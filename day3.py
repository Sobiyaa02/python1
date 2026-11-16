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
   
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,"Fizz Buzz")
#     elif i % 3 == 0:
#         print(i,"Fizz")
#     elif i % 5 == 0:
#         print(i,"Buzz")
#     else:
#         print(i)
    
# Positive=0
# Negative=0
# Zero=0
# for i in range(10):
#     num=int(input("enter a number:"))
#     if num > 0:
#         Positive += 1
#     elif num < 0:
#         Negative += 1
#     else:
#         Zero += 1
# print("Total positive:",Positive)
# print("Total negative:",Negative)
# print("Total zero:",Zero)

# secretnumber=50
# for i in range(5):
#     num=int(input("enter a number:"))
#     if num == secretnumber:
#         print("Correct")
#     elif num > secretnumber:
#         print("Too High")
#     elif num < secretnumber:
#         print("Too Low")
#     else:
#         print("Game Over")

# sum=0
# for i in range(5):
#     marks=int(input("enter a number:"))
#     if marks > 90 and marks < 100:
#         print("A grade")
#         sum += 1
#     elif marks > 75 and marks < 89:
#         print("B grade")
#         sum +=1
#     elif marks > 50 and marks < 74:
#         print("D grade")
#         sum += 1
#     elif marks > 35 and marks < 49:
#         print("D grade")
#         sum += 1
#     else:
#         print("Fail")
#         sum += 1
# print("Total marks:",sum+1)

              
for i in range(1,100):
    if i % 2 == 0 and i % 3 == 0:
        print("Both")
    elif i % 2 == 0:
        print("Two")
    elif i % 3 == 0:
        print("Three")
    else:
        print(i)

    