def is_prime(prime):
    for i in range(2, prime):
        if prime % i == 0:
            return False
    return True

def get_next_prime(prime):
    prime += 1
    while(not is_prime(prime)):
        prime += 1
    return prime

def main():
    prime = 2
    while True:
        response = input("Do you want the next prime? (yN)")
        if response.lower() == 'y':
            print(prime)
            prime = get_next_prime(prime)
        elif response.lower() == 'n':
            break
        else:
            print("Invalid Response")

if __name__ == '__main__':
    main()
