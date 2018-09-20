import random

def main():
    flips = 0
    try:
        flips = int(input("Input number of coin flips: "))
    except ValueError:
        print("Invalid input")
        return None
    results = {'head':0, 'tail':0}
    for i in range(flips):
        if random.uniform(0,1) <= 0.5:
            results['head'] += 1        
        else:
            results['tail'] += 1
    print('heads: ' + str(results['head']), end='\n')
    print('tails: ' + str(results['tail']), end='\n')


if __name__=='__main__':
    main()
