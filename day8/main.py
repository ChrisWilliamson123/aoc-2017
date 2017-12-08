def should_execute(condition, registers):
    cond_reg_value = registers[condition[0]] if condition[0] in registers.keys() else 0
    return eval('%d %s %d' % (cond_reg_value, condition[1], int(condition[2])))

def parse_instruction(i):
    split = i.split(' ')
    change_multiplier = 1 if split[1] == 'inc' else -1
    return (split[0], int(split[2]) * change_multiplier, split[4:])

def main():
    registers = {}
    max_value = 0
    instructions = [line.rstrip() for line in open('input.txt', 'r').readlines()]
    
    for i in instructions:
        (target, amount, cond) = parse_instruction(i)
        if should_execute(cond, registers):
            registers[target] = registers[target] + amount if target in registers.keys() else amount
            if registers[target] > max_value:
                max_value = registers[target]

    print(registers[max(registers, key=registers.get)])
    print(max_value)

if __name__ == '__main__':
    main()
