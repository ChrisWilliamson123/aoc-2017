def get_ring_index(input_number):
    found_ring = False
    ring_index = 1
    start = 1

    while not found_ring:
        end = start + (ring_index * 8) - 1
        
        if start <= input_number <= end:
            found_ring = True
        else:
            ring_index += 1
            start = end + 1

    return (ring_index, start)

def get_anchor_digits(start, ring_index):
    step = ring_index * 2

    right = start + (ring_index - 1)
    top = right + step
    left = top + step
    bottom = left + step

    return [right, top, left, bottom]

def main():
    input_number = 289325

    ring_index, start = get_ring_index(input_number)
    anchors = get_anchor_digits(start, ring_index)
    diffs = map(lambda x: abs(x - input_number), anchors)
    manhattan_distance = min(diffs) + ring_index

    print(manhattan_distance)

if __name__ == '__main__':
    main()
