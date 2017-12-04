from itertools import permutations

def get_permutations(word):
    return set([''.join(p) for p in permutations(word)])

def is_valid_passphrase(phrase):
    words = phrase.split(' ')
    for i in range(0, len(words)):
        permutations = get_permutations(words[i])
        other_words = set(words[i+1:len(words)])
        if len(permutations & other_words) > 0:
            return False
    return True

def main():
    passphrases = [line.rstrip() for line in open('input.txt', 'r').readlines()]

    valid_count = 0
    for passphrase in passphrases:
        if is_valid_passphrase(passphrase):
            valid_count += 1
    print(valid_count)

if __name__ == '__main__':
    main()