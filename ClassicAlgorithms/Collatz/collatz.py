def main():
    n = 0
    try:
        n = int(input("Input starting number: "))
    except ValueError:
        print("Invalid input")
        return None
    count = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n *= 3
            n += 1
        count += 1
    print("Number of moves made: " + str(count))

if __name__=='__main__':
    main()
