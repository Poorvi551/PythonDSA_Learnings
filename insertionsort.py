col=eval(input("Enter collection:"))
for passno in range(1,len(col)):
    i=passno
    while i!=0 and col[i]<col[i-1]:
        col[i-1],col[i]=col[i],col[i-1]
        i=i-1
print(col)