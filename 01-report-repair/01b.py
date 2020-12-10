# What is the product of the three entries that sum to 2020?
with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    numbers = [int(line) for line in lines]
    for a in numbers:
        for b in numbers:
            for c in numbers:
                if(a + b + c) == 2020:
                    print(f"{a} * {b} * {c} = {a*b*c}")