def reallocate(banks):
    largest_bank_size = max(banks)
    largest_bank_index = banks.index(largest_bank_size)

    banks[largest_bank_index] = 0
    current_index = largest_bank_index

    for i in range(0, largest_bank_size):
        current_index = current_index + 1 if current_index < (len(banks)-1) else 0
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
