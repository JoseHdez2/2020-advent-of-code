# How many passwords are valid according to their policies?
with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    valid_passwords = 0
    for (_range, letter, password) in [line.split() for line in lines]:
        _letter = letter[0]
        index_1, index_2 = _range.split("-")
        char_1, char_2 = password[int(index_1)-1], password[int(index_2)-1]
        valid_passwords += 1 if ((char_1 == _letter) ^ (char_2 == _letter)) else 0
    print(valid_passwords)