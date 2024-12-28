
path = "Day04/input.txt"

def read_file(path):
    with open(path, "r") as file:

        grid = []

        linestr = file.readline()
        
        while linestr:
            linestr = linestr.strip()
            linearr = []
            for letter in linestr:
                linearr.append(letter)

            grid.append(tuple(linearr))
            linestr = file.readline()

        return grid

def count_mas(arr):

    count = 0

    height = len(arr) - 1
    width = len(arr[0]) - 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            # A is always the central letter
            if arr[i][j] == "A" and (i >= 1) and (i <= height - 1) and (j >= 1) and (j <= width - 1):
                # We can use sets to just check the diagonals

                diag1 = {"A", arr[i-1][j-1], arr[i+1][j+1]}
                diag2 = {"A", arr[i-1][j+1], arr[i+1][j-1]}

                if {"M", "A", "S"} == diag1 and {"M", "A", "S"} == diag2:
                    count += 1

    return count

grid = read_file(path)
count = count_mas(grid)
print(count)