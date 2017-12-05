def main():
	instructions = [int(line.rstrip()) for line in open('input.txt', 'r').readlines()]
	i = steps = 0

	while i < len(instructions):
		old = i
		i += instructions[i]
		change = -1 if instructions[old] >= 3 else 1
		instructions[old] += change
		steps += 1

	print(steps)

if __name__ == '__main__':
    main()