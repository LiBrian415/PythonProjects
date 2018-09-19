def main():
    try:
        n = int(input("Input desired number in fibonacci sequence: "))
        prev = 1
        pprev = 1
        if(n == 0 or n == 1):
            print(1)
        else:
            while(n >= 2):
                t = prev
                prev += pprev
                pprev = t
                n -= 1
            print(prev)

    except:
        print('Input given is not an integer.')

if __name__ == '__main__':
    main()
