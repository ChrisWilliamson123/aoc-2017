def includes(configs, current_bank):
    try:
        configs.index(current_bank)
        return True
    except:
        return False

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
    seen_configurations = [list(banks)]

    done = False
    reallocations = 0
    
    while not done:
        banks = reallocate(banks)
        reallocations += 1

        if includes(seen_configurations, banks):
            done = True
        else:
            seen_configurations.append(list(banks))
    
    print(reallocations)


if __name__ == '__main__':
    main()