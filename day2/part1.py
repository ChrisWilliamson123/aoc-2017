def main():
    sheet = [line.rsplit('\t') for line in open('input.txt', 'r').read().splitlines()]
    checksum = 0
    for row in sheet:
        row = [int(x) for x in row]
        checksum += (max(row) - min(row))
    print(checksum)

if __name__ == "__main__":
    main()
