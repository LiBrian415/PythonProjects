def main():
    three = 1
    five = 1
    for i in range(1, 101):
        if three == 3 and five == 5:
            print('FizzBuzz')
            three = 1
            five = 1
        elif three == 3:
            print('Fizz')
            three = 1
            five += 1
        elif five == 5:
            print('Buzz')
            five = 1
            three += 1
        else:
            print(i)
            three += 1
            five += 1

if __name__ == '__main__':
    main()
