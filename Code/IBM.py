def minPower(cells):
    # Write your code here
    powers = []
    cells.sort()
    print(cells)
    while (len(cells) > 1):
        curr = cells[0] + cells[1]
        powers.append(curr)
        print(powers)
        cells = cells[2:]
        cells.insert(0, curr)
        cells.sort()
        print(cells)
    return sum(powers)

numbers = [30, 10, 20]
print(minPower(numbers))
