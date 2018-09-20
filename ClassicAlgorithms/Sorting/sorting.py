def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def bubble_sort(lst):
    count = 0
    first = True
    while count > 0 or first:
        first = False
        count = 0
        for i in range(1, len(lst)):
            if lst[i] < lst[i-1]:
                swap(lst, i, i-1)
                count += 1

def merge_combine(lst, l, m, r):
    left = []
    for i in range(l, m+1):
        left.append(lst[i])
    right = []
    for i in range(m+1, r+1):
        right.append(lst[i])
    i = 0
    j = 0
    curr = l
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[curr] = left[i]
            i += 1
        else:
            lst[curr] = right[j]
            j += 1
        curr += 1
    while(i < len(left)):
        lst[curr] = left[i]
        i += 1
        curr += 1
    while(j < len(right)):
        lst[curr] = right[j]
        j += 1
        curr += 1

def merge_sort(lst, l, r):
    if r > l:
        m = l + (r-l)//2
        merge_sort(lst, l, m)
        merge_sort(lst, m+1, r)
        merge_combine(lst, l, m, r)

def main():
    lst = [1,5,2,3,6,4]
    for i in lst:
        print(i, end = ' ')
    print('\n')
    merge_sort(lst, 0, len(lst)-1)
    for i in lst:
        print(i, end = ' ')
    print('\n')
if __name__=='__main__':
    main()
