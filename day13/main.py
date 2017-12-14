import math

def is_caught(depth, range):
    return (depth % (range - 1)) == 0 and math.floor(depth/range) % 2 == 1

def main():
    depths_to_ranges = {}
    for line in open('input.txt', 'r').readlines():
        line = line.rstrip().split(': ')
        depths_to_ranges[int(line[0])] = int(line[1])
    
    severity = 0
    for depth in depths_to_ranges:
        this_range = depths_to_ranges[depth]
        if is_caught(depth, this_range):
            severity += (depth * this_range) 

    print(severity)

if __name__ == '__main__':
    main()