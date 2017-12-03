import sys

def get_neighbour_coords(current_coord):
    coords = set()
    for x in range(current_coord[0]-1, current_coord[0]+2):
        for y in range(current_coord[1]-1, current_coord[1]+2):
            if [x, y] != current_coord:
                coords.add((x, y))
    return coords

def get_ring_coords(ring_index, current_coord):
    coords = []
    current_coord[0] += 1
    coords += [list(current_coord)]
    coords += move_up(ring_index, current_coord)
    coords += move_left(ring_index, current_coord)
    coords += move_down(ring_index, current_coord)
    coords += move_right(ring_index, current_coord)
    return coords

def move_up(ring_index, current_coord):
    coords = []
    while current_coord[1] < ring_index:
        current_coord[1] += 1
        coords.append(list(current_coord))
    return coords

def move_left(ring_index, current_coord):
    coords = []
    while current_coord[0] > ring_index * -1:
        current_coord[0] -= 1
        coords.append(list(current_coord))
    return coords

def move_down(ring_index, current_coord):
    coords = []
    while current_coord[1] > ring_index * -1:
        current_coord[1] -= 1
        coords.append(list(current_coord))
    return coords

def move_right(ring_index, current_coord):
    coords = []
    while current_coord[0] < ring_index:
        current_coord[0] += 1
        coords.append(list(current_coord))
    return coords

def get_coord_sum(coord, coord_sums):
    total = 0
    neighbours = get_neighbour_coords(coord)
    for neighbour in neighbours:
        if (neighbour[0], neighbour[1]) in coord_sums.keys():
            total += coord_sums[(neighbour[0], neighbour[1])]
    coord_sums[(coord[0], coord[1])] = total
    return total

def main():
    n = 289326

    coord_sums = {}
    current_coord = [0,0]
    coord_sums[(current_coord[0], current_coord[1])] = 1

    ring_index = 1
    answer_found = False
    while not answer_found:
        this_ring_coords = get_ring_coords(ring_index, current_coord)
        for coord in this_ring_coords:
            coord_sum = get_coord_sum(coord, coord_sums)
            if coord_sum > n:
                answer_found = True
                answer = coord_sum
                break

        ring_index += 1

    print(answer)


if __name__ == '__main__':
    main()