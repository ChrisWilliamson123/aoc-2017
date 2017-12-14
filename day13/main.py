import math

def is_caught(depth, range):
    steps_to_one = (range-1) * 2
    return depth % steps_to_one == 0

def is_clear_run(depths_to_ranges, delay):
    for depth, range in depths_to_ranges.items():
        if is_caught(depth+delay, range):
            return False
    return True

def main():
    depths_to_ranges = {}

    for line in open('input.txt', 'r').readlines():
        line = line.rstrip().split(': ')
        depths_to_ranges[int(line[0])] = int(line[1])
    
    delay = 0
    clear_run = False

    while not clear_run:
        delay += 1
        clear_run = is_clear_run(depths_to_ranges, delay)

    print('Clear run is achieved with a delay of %d picoseconds' % delay)

if __name__ == '__main__':
    main()