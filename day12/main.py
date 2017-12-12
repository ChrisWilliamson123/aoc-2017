def is_separate_group(groups, id):
    for key in groups:
        if id in groups[key]:
            return False
    return True

def get_connections(direct_lines, id):
    to_check = [id]
    checked = set()

    while len(to_check) > 0:
        current = to_check[-1]
        neighbours = direct_lines[current]
        to_check = to_check[0:-1]

        for n in neighbours:
            if n not in checked and n not in to_check:
                to_check.insert(0, n)
        checked.add(current)
    return checked

def main():
    direct_lines = {}
    groups = {}
    for l in open('input.txt', 'r').readlines():
        l = l.rstrip()
        split = l.split(' <-> ')
        direct_lines[int(split[0])] = [int(x) for x in split[1].split(', ')]

    for i in range(0, len(direct_lines)):
        if is_separate_group(groups, i):
            groups[i] = get_connections(direct_lines, i)

    print('Part one: %d' % len(groups[0]))
    print('Part two: %d' % len(groups))


if __name__ == '__main__':
    main()