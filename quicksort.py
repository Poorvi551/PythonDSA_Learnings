def sorted_pos(col,low,high):
    pivot=col[low]
    i=low+1
    j=high
    while i<=j:
        while i<=j and col[i]<pivot:
            i=i+1
        while i<=j and col[j]>pivot:
            j=j-1
        if i<j:
            col[i],col[j]=col[j],col[i]
    col[j],col[low]=col[low],col[j]
    return j
def quick_sort(col,low,high):
    if low>high:
        return
    sp=sorted_pos(col,low,high)
    quick_sort(col,low,sp-1)
    quick_sort(col,sp+1,high)
col=eval(input("Enter list:"))
quick_sort(col,0,len(col)-1)
print(col)
