with open('input.txt', 'r') as f:
    dat = f.read()

# Convert to list of integer inventories, then sums
inventories = dat.split(sep="\n\n")
inventories = [inv.splitlines() for inv in inventories]
inventories = [[int(num) for num in inv] for inv in inventories]

sums = [sum(inv) for inv in inventories]

# Find largest calorie sum
largest = max(sums)
# assumes calorie sums are unique
elf_no = sums.index(largest)
print(f"Elf {elf_no} had the largest calorie inventory at {largest}.")

# Part two
# sum of top 3.
sums.sort(reverse = True)
top_3_sum = sum(sums[:3])
print(f"The top 3 elves in terms of calorie inventory held altogether {top_3_sum} calories.")
