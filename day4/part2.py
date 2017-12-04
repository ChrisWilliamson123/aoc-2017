def is_valid_passphrase(phrase):
    sorted_words = [''.join(sorted(w)) for w in phrase.split(' ')]
    if len(set(sorted_words)) == len(sorted_words):
        return True
    return False

def main():
    passphrases = [line.rstrip() for line in open('input.txt', 'r').readlines()]

    valid_count = 0
    for passphrase in passphrases:
        if is_valid_passphrase(passphrase):
            valid_count += 1
    print(valid_count)

if __name__ == '__main__':
    main()