def get_next_index(number_list, current_index, step):
    nextIndex = current_index + step

    if nextIndex > len(number_list)-1:
        return nextIndex - len(number_list)

    return nextIndex

def main():
    inputString = open('input.txt', 'r').read()
    step = len(inputString) / 2

    total = 0
    for i in range(0, len(inputString)):
        nextIndex = get_next_index(inputString, i, step)

        if inputString[i] == inputString[nextIndex]:
            total += int(inputString[i])

    print(total)

if __name__ == '__main__':
    main()
