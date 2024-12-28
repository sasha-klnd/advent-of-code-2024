import math

path = "Day05/test-input.txt"

def get_rules(path):

    rules = []

    try:
        with open(path, "r") as file:

            line = file.readline()

            while line:
                if "|" in line:
                    line = line.strip('\n')
                    rule = line.split("|")
                    for i in range(len(rule)):
                        rule[i] = int(rule[i])

                    rules.append(tuple(rule))
                    line = file.readline()
                else:
                    break
    except Exception:
        print("Exception")
    return tuple(rules)

def get_updates(path):

    updates = []

    try:
        with open(path, "r") as file:

            line = file.readline()
            
            # Find blank line between rules and updates
            while line != "\n":
                line = file.readline()
            
            line = file.readline()
            
            while line:
                line = line.strip('\n')
                update = line.split(',')

                for i in range(len(update)):
                    update[i] = int(update[i])

                updates.append(tuple(update))
                line = file.readline()
            
    except Exception:
        print("Exception")

    return tuple(updates)

def get_incorrect_updates(rules, updates):

    incorrect_updates = []

    for i in range(len(updates)):
        # For each update we want all the applicable rules

        applicable_rules = []

        for rule in rules:
            if (rule[0] in updates[i]) and (rule[1] in updates[i]) and (rule not in applicable_rules):
                applicable_rules.append(rule)

        update_is_valid = True

        for j in range(len(applicable_rules)):
            first, last = applicable_rules[j][0], applicable_rules[j][1]
            if updates[i].index(first) > updates[i].index(last):
                update_is_valid = False

        if not update_is_valid:
            incorrect_updates.append(updates[i])

    return incorrect_updates

rules = get_rules(path)
updates = get_updates(path)
incorrect_updates = get_incorrect_updates(rules, updates)

middle_sum = 0

for update in incorrect_updates:
    middle_sum += update[int(len(update) / 2)]

print(incorrect_updates)