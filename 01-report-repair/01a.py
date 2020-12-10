# Find the two entries that sum to 2020; what do you get if you multiply them together?
with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    numbers = [int(line) for line in lines]
    for a in numbers:
        for b in numbers:
            if(a + b) == 2020:
                print(f"{a} * {b} = {a*b}")