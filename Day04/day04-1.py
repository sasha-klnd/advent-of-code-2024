
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

def count_xmas(arr):

    count = 0

    height = len(arr) - 1
    width = len(arr[0]) - 1

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X":
                # Check each direction fully
                # Up
                if i >= 3:
                    if (arr[i-1][j] == "M") and (arr[i-2][j] == "A") and (arr[i-3][j] == "S"):
                        count += 1
                # Up Right
                if i >= 3 and j <= (width - 3):
                    if (arr[i-1][j+1] == "M") and (arr[i-2][j+2] == "A") and (arr[i-3][j+3] == "S"):
                        count += 1
                # Right
                if j <= (width - 3):
                    if (arr[i][j+1] == "M") and (arr[i][j+2] == "A") and (arr[i][j+3] == "S"):
                        count += 1
                # Down Right
                if i <= (height - 3) and j <= (width - 3):
                    if (arr[i+1][j+1] == "M") and (arr[i+2][j+2] == "A") and (arr[i+3][j+3] == "S"):
                        count += 1
                # Down
                if i <= (height - 3):
                    if (arr[i+1][j] == "M") and (arr[i+2][j] == "A") and (arr[i+3][j] == "S"):
                        count += 1  
                # Down Left
                if i <= (height - 3) and j >= 3:
                    if (arr[i+1][j-1] == "M") and (arr[i+2][j-2] == "A") and (arr[i+3][j-3] == "S"):
                        count += 1
                # Left
                if j >= 3:
                    if (arr[i][j-1] == "M") and (arr[i][j-2] == "A") and (arr[i][j-3]== "S"):
                        count += 1
                # Up Left
                if i >= 3 and j >= 3:
                    if (arr[i-1][j-1] == "M") and (arr[i-2][j-2] == "A") and (arr[i-3][j-3] == "S"):
                        count += 1

    return count

grid = read_file(path)
count = count_xmas(grid)
print(count)