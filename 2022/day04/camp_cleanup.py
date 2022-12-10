with open('input.txt') as f:
    dat = f.read()

assignments = [x.split(',') for x in dat.splitlines()]

def assignment_to_set(a):
    start = int(a[:a.find('-')])
    end = int(a[a.find('-')+1:])
    # range stops at arg2 - 1
    return set(range(start, end+1))

assignments_setted = [[assignment_to_set(y) for y in x] for x in assignments]

subset_test_results = [x[0].issubset(x[1]) or x[0].issuperset(x[1]) for x in assignments_setted]

num_contain_pairs = sum(subset_test_results)
print(f"{num_contain_pairs} pairs have a range that contains the other.")

# part 2
overlap_test_results = [len(x[0].intersection(x[1])) != 0 for x in assignments_setted]
num_overlap = sum(overlap_test_results)
print(f"{num_overlap} pairs have some overlap.")


