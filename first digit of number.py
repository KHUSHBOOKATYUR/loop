num=int(input("enter the number-:"))
i=1
while i<=num:
    a=1
    a=(num%10)
    num//=10
    i=i+1
print(a)

