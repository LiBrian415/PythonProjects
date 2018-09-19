import math

def calculate_pi(round_val):
    return '%.*f' %(round_val, math.pi)

def shell():
    val = input("Input the number of digits of pi you want:(up to 48) ")
    n = 0
    try:
        n = int(val)
        print(calculate_pi(n))
    except:
        print("Input was not an integer.")



if __name__ == "__main__":
    shell()
