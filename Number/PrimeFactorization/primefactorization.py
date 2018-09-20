def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(prime, num):
    if is_prime(num):
        return num
    else:
        prime+=1
        while not isPrime(prime) and prime < num:
            prime+=1
        return prime

def main():
    n = 0
    try:
        n = int(input("Input an integer: "))
    except:
        print("Input is not an integer.")
        return None
    prime = 2
    list = []
    while n > 1:
        if n % prime == 0:
            list.append(prime)
            n //= prime
        else:
            prime = get_next_prime(prime, n)

    for i in list:
        print(i, end=" ") 
    print('\n')

if __name__ == '__main__':
    main()
