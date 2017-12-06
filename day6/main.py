def get_busiest_bank(banks):
    largestAmount = max(banks)
    return (banks.index(largestAmount), largestAmount)

def get_next_index(banks, current_index):
    if current_index == (len(banks) - 1):
        return 0
    return current_index + 1

def reallocate(banks):
    busiest_index, size = get_busiest_bank(banks)
    banks[busiest_index] = 0
    current_index = busiest_index
    for i in range(0, size):
        current_index = get_next_index(banks, current_index)
        banks[current_index] += 1

    return banks

def main():
    banks = [int(block) for block in open('input.txt', 'r').read().split('\t')]
    seen_configurations = {}
    reallocations = 0

    while str(banks) not in seen_configurations:
        seen_configurations[str(banks)] = reallocations
        banks = reallocate(banks)
        reallocations += 1
    
    print('Reallocations: %d' % reallocations)
    print('Reallocations between matched banks: %d' % (reallocations - seen_configurations[str(banks)]))

if __name__ == '__main__':
    main()
