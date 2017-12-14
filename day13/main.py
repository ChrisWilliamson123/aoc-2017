import math

def main():
    depths_to_ranges = {}
    for line in open('input.txt', 'r').readlines():
        line = line.rstrip().split(': ')
        depths_to_ranges[int(line[0])] = int(line[1])
    
    severity = 0
    for depth in depths_to_ranges:
        this_range = depths_to_ranges[depth]
        if (depth % (this_range - 1)) == 0 and math.floor(depth/this_range) % 2 == 1:
            severity += (depth * this_range) 

    print(severity)

if __name__ == '__main__':
    main()