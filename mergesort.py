def merge_sort(l):
    if len(l) > 1:
        left = l[:len(l)//2]
        right = l[len(l)//2:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i = i + 1
            else:
                l[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            l[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            l[k] = right[j]
            j = j + 1
            k = k + 1

l = eval(input("Enter list:"))
merge_sort(l)
print(l)