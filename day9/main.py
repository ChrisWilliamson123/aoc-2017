import re

def cancel_character(stream, index):
    cancel_count = 0
    prev_char = stream[index-1]
    while prev_char is '!':
        cancel_count += 1
        index -= 1
        prev_char = stream[index-1]
    return False if cancel_count % 2 is 0 else True

def main():
    stream = open('input.txt', 'r').read()
    depth = score = garbage_char_count = 0
    in_garbage = False

    for i in range(0, len(stream)):
        if not cancel_character(stream, i):
            char = stream[i]

            if in_garbage and char not in ['!', '>']:
                garbage_char_count += 1
            elif not in_garbage:
                if char is '{':
                    depth += 1
                elif char is '}' and depth > 0:
                    score += depth
                    depth -= 1
                
            if char is '<':
                in_garbage = True
            elif char is '>':
                in_garbage = False
      
    print(score, garbage_char_count)

if __name__ == '__main__':
    main()