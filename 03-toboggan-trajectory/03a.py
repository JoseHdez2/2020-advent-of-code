# Starting at the top-left corner of your map and following a slope of right 3 and down 1,
# how many trees would you encounter?
with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    x_pos = 0
    trees = 0
    width = len(lines[0])
    for line in lines:
        trees += 1 if (line[x_pos] == "#") else 0
        x_pos += 3
        x_pos %= width
    print(trees)