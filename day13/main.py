import math

def is_caught(depth, range):
    return (depth % (range - 1)) == 0 and math.floor(depth/range) % 2 == 1

def main():
    depths_to_ranges = {}
    for line in open('input.txt', 'r').readlines():
        line = line.rstrip().split(': ')
        depths_to_ranges[int(line[0])] = int(line[1])
    
    severity = 0
    for depth, range in depths_to_ranges.items():
        if is_caught(depth, range):
            severity += (depth * range) 

    print(severity)

if __name__ == '__main__':
    main()