def main():
    s = input("Input the string you want to reverse: ")
    lst = list(s)
    l = 0
    r = len(lst) - 1
    while r > l:
        temp = lst[l]
        lst[l] = lst[r]
        lst[r] = temp
        l += 1
        r -= 1
    print("".join(lst))

if __name__ == '__main__':
    main()
