# What do you get if you multiply together the number of trees encountered on each of the listed slopes?
with open('input.txt') as f:
    lines = f.read().splitlines()
    print(lines)

    x,y = [0,0]
    width = len(lines[0])
    slopes = [1,1], [3,1], [5,1], [7,1], [1,2]
    dict_trees = {}
    for slope in slopes:
        trees = 0
        while y > len(lines):
            trees += 1 if (lines[y][x] == "#") else 0
            x += slope[0]
            x %= width
            y + slope[1]
        dict_trees[str(slope)] = trees

    result = 1
    for v in dict_trees.values():
        result *= v
    print(dict_trees.values())