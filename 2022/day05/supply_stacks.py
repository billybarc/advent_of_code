# data import
with open("input.txt") as f:
    dat = f.read()

stack_data, steps = dat.split("\n\n")

steps = steps.splitlines()

# get stack data into list of lists
import re
n_stacks = max([int(x) for x in re.findall('[0-9]+', stack_data)])
stack_data = stack_data.splitlines()
# get rid of line of stack indices
stack_data = stack_data[:(len(stack_data)-1)]

stacks = [[] for i in range(n_stacks)]
stack_data_flipped = stack_data[::-1]
for line in stack_data_flipped:
    for match in re.finditer('[A-Z]', line):
        # crate size and spacing hard coded into the 4 here
        ind = (match.start() - 1) // 4
        stacks[ind].append(match.group())

# for part 2
import copy
stacks2 = copy.deepcopy(stacks)

# do the crate moves
for op in steps:
    (num, from_, to_) = (int(match.group()) for match in re.finditer("[0-9]+", op))
    from_ -= 1
    to_ -= 1
    for n in range(num):
        x = stacks[from_].pop()
        stacks[to_].append(x)

def get_top_crates(l):
    return "".join([stack.pop() for stack in l])

print(get_top_crates(stacks))


# part 2
for op in steps:
    (num, from_, to_) = (int(match.group()) for match in re.finditer("[0-9]+", op))
    from_ -= 1
    to_ -= 1
    x = []
    for n in range(num):
        x.append(stacks2[from_].pop())
    x.reverse()
    stacks2[to_].extend(x)

print(get_top_crates(stacks2))
