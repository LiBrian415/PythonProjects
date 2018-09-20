def main():
    s = input("Input a string: ")
    l = 0
    r = len(s) - 1
    while r > l:
        if s[r] != s[l]:
            print("Not a palindrome")
            return None
        l += 1
        r -= 1
    print("Is a palindrome")

if __name__ == '__main__':
    main()
