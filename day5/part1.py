def main():
	instructions = [int(line.rstrip()) for line in open('input.txt', 'r').readlines()]
	i = steps = 0

	while i < len(instructions):
		old = i
		i += instructions[i]
		instructions[old] += 1
		steps += 1

	print(steps)

if __name__ == '__main__':
    main()