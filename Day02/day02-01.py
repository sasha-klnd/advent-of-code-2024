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
num_safe_reports_damp = 0

def is_safe(report):
    distances = []

    for i in range(1, len(report)):
        distances.append(report[i] - report [i-1])
    
    multi_direction = False
    invalid_distance = False

    # Check for all distances between 1 and 3
    for val in distances:
        if abs(val) < 1 or abs(val) > 3:
            invalid_distance = True
    
    # Check for all distances in the same direction
    if distances[0] < 0:
        for val in distances:
            if val > 0:
                multi_direction = True
    
    if distances[0] > 0:
        for val in distances:
            if val < 0:
                multi_direction = True
    
    # Report is safe if both conditions are false:
    if not multi_direction and not invalid_distance:
        return True
    else:
        return False

for report in reports:
    if is_safe(report):
        num_safe_reports += 1

print(num_safe_reports)