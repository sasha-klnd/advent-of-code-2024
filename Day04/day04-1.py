
path = "Day04/input.txt"

def process_input(path):
    with open(path, "r") as file:
        data = file.read()

        rows = data.split("\n")

        for i in range(len(rows)):
            cols = []
            for letter in rows[i]:
                cols.append(letter)
            rows[i] = cols
        return rows

arr = process_input(path)
width = len(arr[0])
height = len(arr)

def search_surrounding(arr, i, j):
    # Call when X is found
    width = len(arr[0])
    height = len(arr)

    directions = {}
    matches = []

    directions["t"] = arr[i-1][j] if (i > 2) else '0'
    directions["tr"] = arr[i-1][j+1] if (i > 2 and j < (width-3)) else '0'
    directions['r'] = arr[i][j+1] if j < (width-3) else '0'
    directions['br'] = arr[i+1][j+1] if (i < (height-3) and j < (width-3)) else '0'
    directions['b'] = arr[i+1][j] if (i < (height-3)) else '0'
    directions['bl'] = arr[i+1][j-1] if (i < (height-3) and j > 2) else '0'
    directions['l'] = arr[i][j-1] if (j > 2) else '0'
    directions['tl'] = arr[i-1][j-1] if (i > 2 and j > 2) else '0'

    for direction in tuple(directions.keys()):
        if directions[direction] == "M":
            matches.append(direction)
    
    return matches

def full_search(arr, i, j, directions):
    matches = 0

    for direction in directions:
        if direction == "t":
            if arr[i][j] == "X" and arr[i-1][j] == "M" and arr[i-2][j] == "A" and arr[i-3][j] == "S":
                matches += 1
        elif direction == "tr":
            if arr[i][j] == "X" and arr[i-1][j+1] == "M" and arr[i-2][j+2] == "A" and arr[i-3][j+3] == "S":
                matches += 1
        elif direction == "r":
            if arr[i][j] == "X" and arr[i][j+1] == "M" and arr[i][j+2] == "A" and arr[i][j+3] == "S":
                matches += 1
        elif direction == "br":
            if arr[i][j] == "X" and arr[i+1][j+1] == "M" and arr[i+2][j+2] == "A" and arr[i+3][j+3] == "S":
                matches += 1
        elif direction == "b":
            if arr[i][j] == "X" and arr[i+1][j] == "M" and arr[i+2][j] == "A" and arr[i+3][j] == "S":
                matches += 1
        elif direction == "bl":
            if arr[i][j] == "X" and arr[i+1][j-1] == "M" and arr[i+2][j-2] == "A" and arr[i+3][j-3] == "S":
                matches += 1
        elif direction == "l":
            if arr[i][j] == "X" and arr[i][j-1] == "M" and arr[i][j-2] == "A" and arr[i][j-3] == "S":
                matches += 1
        elif direction == "tl":
            if arr[i][j] == "X" and arr[i-1][j-1] == "M" and arr[i-2][j-2] == "A" and arr[i-3][j-3] == "S":
                matches += 1

    return matches


for i in range(height):
    for j in range(width):
        if arr[i][j] == "X":
            directions = search_surrounding(arr, i, j)

            if directions:
                matches = full_search(arr, i, j, directions)



print(matches)