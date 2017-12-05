def main():
	instructions = [int(line.rstrip()) for line in open('input.txt', 'r').readlines()]
	i = steps = 0

	while i < len(instructions):
		old = i
		i += instructions[i]
		if instructions[old] >= 3:
			instructions[old] -=1
		else:
			instructions[old] += 1
		steps += 1

	print(steps)

if __name__ == '__main__':
    main()