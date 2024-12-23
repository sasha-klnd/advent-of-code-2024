# Advent of Code Day 1
import math

def parseLine(string):
    end_of_num1 = string.find(" ")

    num1 = string[0:end_of_num1]
    if num1.isdigit():
        num1 = int(num1)
    
    start_of_num2 = string.rfind(" ") + 1
    end_of_num2 = string.find("\n")


    num2 = string[start_of_num2:end_of_num2]
    if num2.isdigit():
        num2 = int(num2)

    return (num1, num2)

def fileRead(path):
    list1 = []
    list2 = []

    try:
        with open(path, "r") as file:
            line = file.readline()

            while line:
                nums = parseLine(line)
                list1.append(nums[0])
                list2.append(nums[1])
                line = file.readline()
    except FileNotFoundError:
        print("FileNotFoundError")
    except PermissionError:
        print("PermissionError")

    return (list1, list2)

# Read file and sort lists
lists = fileRead("Day01/input.txt")
list1 = sorted(lists[0])
list2 = sorted(lists[1])

# Compare distances

total_distance = 0

for i in range(len(list1)):
    distance = abs(list1[i] - list2[i])
    total_distance += distance

print(total_distance)