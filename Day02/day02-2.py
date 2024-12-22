import math
path = "Day02/input.txt"

def read_file(path):
    with open(path, "r") as file:
        inpt = file.read()

        lines = inpt.splitlines()

        for i in range(len(lines)):
            lines[i] = lines[i].strip().split(" ")
        
        for line in lines:
            for j in range(len(line)):
                line[j] = int(line[j])

        return lines

reports = read_file(path)
num_safe_reports = 0

def is_safe(report):
    expected_direction = math.copysign(1, report[1] - report[0])

    for i in range(1, len(report)):
        distance = report[i] - report[i-1]

        if not math.copysign(1, distance) == expected_direction:
            return False
        
        elif abs(distance) > 3 or abs(distance) < 1:
            return False
    
    return True

def is_safe_with_dampener(report):
    
    for i in range(len(report)):
        dampened_report = list(report)
        dampened_report.pop(i)
        if is_safe(dampened_report):
            return True
    
    return False

for report in reports:
    if is_safe_with_dampener(report):
        num_safe_reports += 1

print(num_safe_reports)