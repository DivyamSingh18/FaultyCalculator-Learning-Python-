print("write two nos. to perform calculation!!!")
a = int(input())
b = int(input())


print("What operation u want to perform (sum/mul/div/sub)")
op = input()

if (a==2 and b==2 and op =="sum"):
    print(5)
elif (a==5 and b==10 and op =="mul"):
    print(49)
elif (a==10 and b==5 and op =="mul"):
    print(49)

elif op == "sum":
    print(a+b)
elif op == "sub":
    print(a-b)
elif op == "mul":
    print(a*b)
elif op == "div":
    print(a/b)
else:
    print("NOT SUPPORTED (Invalid)")