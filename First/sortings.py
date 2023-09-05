# Bubble sort
l = [8, 7, 4, 6, 5, 3]
for i in range(len(l)):
    for j in range(len(l) - 1 - i):
        if l[j] > l[j + 1]:
            # swap
            t = l[j]
            l[j] = l[j + 1]
            l[j + 1] = t
print(l)

# Selection sort
l = [8, 7, 4, 6, 5, 3]
for i in range(0,len(l)):
    for j in range(i, len(l)):
        minimum_value = l[i]
        minimum_value_index = i
        if (l[j] < minimum_value):
            minimum_value_index = j
            minimum_value = l[j]
        #swap
        t = l[i]
        l[i] = minimum_value
        l[minimum_value_index] = t
print(l)


#Merge sort
l = [8, 7, 4, 6, 5, 3]
def merge_sort(l, start, end):
    if(end>start):
        merge_sort(l, start, (start+end)//2)
        merge_sort(l, (start+end)//2+1, end)
        merge(l, start,(start+end)//2, end)
def merge(l, start, mid, end):
    tl = []
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if l[i] <= l[j]:
            tl.append(l[i])
            i += 1
        else:
            tl.append(l[j])
            j += 1
    while i <= mid:
        tl.append(l[i])
        i += 1
    while j <= end:
        tl.append(l[j])
        j += 1
    j = 0
    for i in range(start, end+1):
        l[i] = tl[j]
        j += 1
merge_sort(l, 0, len(l)-1)
print(l)