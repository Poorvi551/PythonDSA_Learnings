col=eval(input("Enter collection:"))
for passno in range(1,len(col)):
    minp=passno-1
    for i in range(passno,len(col)):
        if col[i]<col[minp]:
            minp=i
    col[passno-1],col[minp]=col[minp],col[passno-1]
print(col)