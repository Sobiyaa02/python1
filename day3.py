# for i in range(1,21):
#     if i % 2 == 0:
#         print(i,"even number")
#     else:
#         print(i,"odd number")

num=int(input("enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
    if i % num == 0:
        print("even")
    else:
        print("odd")
