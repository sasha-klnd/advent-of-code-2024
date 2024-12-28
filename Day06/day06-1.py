
path = "Day06/input.txt"

def process_input(path):
    with open(path, 'r') as file:
        
        map = []

        line = file.readline()
        while line:
            line = line.strip()
            map.append(list(line))
            line = file.readline()
        
        return map

def turn(current_dir):
    # Turns the guard 90 degrees clockwise
    match current_dir:
        case '^':
            return '>'
        case '>':
            return 'v'
        case 'v':
            return '<'
        case '<':
            return '^'

def find_trajectory(map):
    position = [0,0]
    next_position = [0,0] 
    direction = '^'
    visited_tiles = 0

    # Find initial guard position
    for i in range(len(map)):
        if '^' in map[i]:
            position[1] = map[i].index('^')
            position[0] = i
            break

    while True:
        # Get next tile
        if direction == '^':
            next_position[0] = position[0] - 1
            next_position[1] = position[1]
        
        elif direction == '>':
            next_position[0] = position[0]
            next_position[1] = position[1] + 1
        
        elif direction == 'v':
            next_position[0] = position[0] + 1
            next_position[1] = position[1]

        elif direction == '<':
            next_position[0] = position[0] 
            next_position[1] = position[1] - 1


        if not (next_position[0] >= 0 and next_position[0] < len(map) and next_position[1] >= 0 and next_position[1] < len(map[0])):
            break
        elif map[next_position[0]][next_position[1]] == '#':
            direction = turn(direction)
            map[position[0]][position[1]] = direction
        else:
            map[next_position[0]][next_position[1]] = direction
            map[position[0]][position[1]] = 'X'
            position[0], position[1] = next_position[0], next_position[1]
    
    map[position[0]][position[1]] = 'X'

    for row in map:
        visited_tiles += row.count("X")

    return visited_tiles

map = process_input(path)
visited_tiles = find_trajectory(map)
print(visited_tiles)