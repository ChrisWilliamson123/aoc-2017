def main():
    sheet = [line.rsplit('\t') for line in open('input.txt', 'r').read().splitlines()]
    checksum = 0
    for row in sheet:
        row = sorted([int(x) for x in row], reverse=True)
        for i in range(0, len(row)):
            for j in range(len(row)-1, i, -1):
                if (row[i] % row[j]) == 0:
                    checksum += row[i] / row[j]
    print(checksum)

if __name__ == "__main__":
    main()
