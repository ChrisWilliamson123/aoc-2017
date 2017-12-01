def main():
    inputString = open('input.txt', 'r').read()
    step = len(inputString) / 2

    total = 0
    for i in range(0, len(inputString)):
        nextIndex = i + step

        if nextIndex > len(inputString)-1:
            nextIndex = nextIndex - len(inputString)

        if inputString[i] == inputString[nextIndex]:
            total += int(inputString[i])

    print(total)

if __name__ == '__main__':
    main()
