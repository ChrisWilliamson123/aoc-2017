def should_execute(condition, registers):
    cond_reg_value = registers[condition[0]] if condition[0] in registers.keys() else 0
    return eval('%d %s %d' % (cond_reg_value, condition[1], int(condition[2])))

def parse_instruction(i):
    split = i.split(' ')
    target = split[0]
    change_amount = int(split[2])
    change_multiplier = 1 if split[1] == 'inc' else -1
    cond = split[4:]
    return [target, change_amount * change_multiplier, cond]

def main():
    registers = {}
    instructions = [line.rstrip() for line in open('input.txt', 'r').readlines()]
    
    for i in instructions:
        i = parse_instruction(i)
        target = i[0]
        amount = i[1]
        condition = i[2]
        if should_execute(condition, registers):
            registers[target] = registers[target] + amount if target in registers.keys() else amount

    print(registers[max(registers, key=registers.get)])

if __name__ == '__main__':
    main()
