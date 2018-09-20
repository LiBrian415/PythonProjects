import math

def main():
    try:
        cost = int(input("Input cost per tile: "))
        floor_width = int(input("Input floor width: "))
        floor_length = int(input("Input floor length: "))
        tile_width = int(input("Input tile width: "))
        tile_length = int(input("Input tile length: "))
        w = math.ceil(floor_width / tile_width)
        l = math.ceil(floor_length / tile_length)
        print(w*l*cost)
    except:
        print("Invalid input")

if __name__ == '__main__':
    main()
