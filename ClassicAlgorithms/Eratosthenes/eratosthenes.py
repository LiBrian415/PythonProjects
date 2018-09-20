def main():
    n = 0
    try: 
        n = int(input("Input ceil number: "))
    except ValueError:
        print("Invalid input.")

    if(n < 2):
        print("No primes found.")
    else:
        result = []
        non_primes = set()
        prime = 2
        while prime <= n:
            if prime not in non_primes:
                result.append(prime)
            num = prime
            while num <= n:
                num += prime
                if num not in non_primes:
                    non_primes.add(num)
            prime += 1
        for i in result:
            print(i, end = ' ')
        print('\n')

            

if __name__ == '__main__':
    main()
