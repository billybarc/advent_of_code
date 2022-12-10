with open("input.txt") as f:
    dat = f.read()

rucksacks = dat.splitlines()

# split into compartments
rucksacks_compartmentalized = [[x[:int(len(x)/2)], x[int(len(x)/2):]] for x in rucksacks]

# we are told only a single item is repeated, so intersection guaranteed
# to be singleton
repeated_items = [set(x[0]).intersection(set(x[1])).pop() for x in rucksacks_compartmentalized]

a_val = ord('a') - 1
A_val = ord('A') - 27

def get_priority(letter):
    if letter.islower():
        return ord(letter) - a_val
    elif letter.isupper():
        return ord(letter) - A_val
    else:
        return ValueError("Only a-zA-Z accepted")

priorities = [get_priority(x) for x in repeated_items]
priority_sum = sum(priorities)
print(f"The priority sum is {priority_sum}.")

# part 2
rucksacks_grouped = [rucksacks[i:(i+3)] for i in range(0, len(rucksacks), 3)]
# convert to sets
rucksacks_grouped_setted = [[set(y) for y in x] for x in rucksacks_grouped]
badges = [set.intersection(*x).pop() for x in rucksacks_grouped_setted]
priority_sum = sum([get_priority(x) for x in badges])
print(f"Badge priority sum is {priority_sum}.")
