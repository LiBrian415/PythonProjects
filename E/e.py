import math

def calculate_e(round_val):
   return '%.*f' %(round_val, math.e)

def main():
    val = input('Input number of digits of e required: (up to 48)')
    try:
        n = int(val)
        print(calculate_e(n))
    except:
        print('Input is not a number')

if __name__ == '__main__':
    main()
