# for i in range (6):
#     for n in range (7):
#         if (i==0 and n%3!=0) or (i==1 and n%5==0) or (i-n==3) or (i+n==9):
#             print ("*",end="")
#         else:
#             print("",end ="")
#     print()


# for i in range (7):
#     for n in range (8):
#         if (i==0 and n%3!=0) or (i==1 and n%3==0) or (i-n==3) or (i+n==9):
#             print ("*",)
#         else:
#             print("",)
#     print()

i=7
n=8
while i<=n:
    count=1     
    while n>=i:
        count=count+1
        if (i==0 and n%3!=0) or (i==1 and n%3==0) or (i-n==3) or (i+n==8):
            print("*",end="")
        else:
            print("",)
    print()
    i=i+1