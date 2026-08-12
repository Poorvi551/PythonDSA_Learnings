# Ternary Search

def ternary_search(col,key):
    li=0
    hi=len(col)-1
    while li<=hi:
        mid1=li+(hi-li)//3
        mid2=hi-(hi-li)//3
        if key==col[mid1]:
            return mid1
        if key==col[mid2]:
            return mid2
        if key<col[mid1]:
            hi=mid1-1
        elif key>col[mid2]:
            li=mid2+1
        else:
            li=mid1+1
            hi=mid2-1
    return -1
col=eval(input("Enter collection:"))
key= int(input("Enter the value:"))
print(ternary_search(col,key))