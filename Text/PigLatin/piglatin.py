def main():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    inp = input("Input a string: ")
    lst = inp.split()
    for index in range(0, len(lst)):
        s = lst[index]
        temp = list(s)
        i = 0
        while s[i].lower() not in vowels:
            i += 1
        lst[index] = s[i:]+s[0:i]+'ay'
    print (" ".join(lst))
    
if __name__ == '__main__':
    main()
