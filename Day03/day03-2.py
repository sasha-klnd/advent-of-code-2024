path = "Day03/input.txt"

def process_input(path):
    with open(path, "r") as file:
        data = file.read()
        return data

def find_mul_in_chunk(chunk):
    if len(chunk) < 5:
        return 0

    if not chunk[0:4] == "mul(":
        return 0

    # Find closing parenthesis
    closing = chunk.find(")")

    if closing == -1:
        return 0
    else:
        chunk = chunk[0:closing]

    # Separate comma
    comma = chunk.find(",")
    arg1 = chunk[4:comma]
    arg2 = chunk[comma+1:]

    if not arg1.isdigit():
        return 0
    elif not arg2.isdigit():
        return 0
    else:
        arg1 = int(arg1)
        arg2 = int(arg2)
        return arg1 * arg2

def next_m(data):
    if data:
        for i in range(1, len(data)):
            if data[i] == 'm':
                break
            else:
                i += 1
    return i

data = process_input(path)
sum = 0
toggle = True
blocks = []

while len(data) > 0:
    if toggle:
        d = data.find("don't()")
        blocks.append(data[0:d])
        data = data[d:]
        toggle = False

    if not toggle:
        d = data.find("do()")
        data = data[d + 4:]
        toggle = True

for block in blocks:
    while len(block) > 0:
        delim = next_m(block)
        chunk = block[:delim]
        block = block[delim:]
        sum += find_mul_in_chunk(chunk)

print(sum)