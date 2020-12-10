with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    valid_passwords = 0
    for (_range, letter, password) in [l.split() for l in lines]:
        count = password.count(letter[0])
        min, max = _range.split("-")
        valid_passwords += 1 if (count in range(int(min), int(max)+1)) else 0
    print(valid_passwords)