def main():
    rope_len = 256
    original = [x for x in range(0, rope_len)]
    rope = [x for x in range(0, rope_len)]
    lengths = [18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188]
    rope_index = 0
    skip_size = 0
    for length in lengths:
        if length > 1:
            end_index = (rope_index + length) % (rope_len)
            if end_index < length:
                section = (rope[rope_index:] + rope[0:end_index])[::-1]
                indexes = original[rope_index:] + original[0:end_index]
            else:
                section = rope[rope_index:end_index][::-1]
                indexes = original[rope_index:end_index]
            
            for i in range(0, length):
                rope[indexes[i]] = section[i]

        rope_index = (rope_index + length + skip_size) % (rope_len)
        skip_size += 1
    
    print(rope[0] * rope[1])

if __name__ == '__main__':
    main()