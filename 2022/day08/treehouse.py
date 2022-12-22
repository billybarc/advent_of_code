
import numpy as np
from math import prod

with open("input.txt") as f:
    dat = f.read()

dat = dat.splitlines()
# list of int lists
dat = [[int(y) for y in list(x)] for x in dat]
dat = np.array(dat)

# all edge treees are visible
n_exterior = (dat.shape[0] - 2 + dat.shape[1] - 2) * 2 + 4

n_interior = 0
# an internal tree is visible if it is the max looking outward from
# at least one direction
for r in range(1, dat.shape[0]-1):
    for c in range(1, dat.shape[1]-1):
        height = dat[r,c]

        up, down, left, right = dat[:r,c], dat[r+1:,c], dat[r,:c], dat[r,c+1:]
        for dir in up, down, left, right:
            if height > max(dir):
                n_interior += 1
                break

print(f"Total visible trees: {n_exterior + n_interior}")

# part 2
scenic_score = 0
for r in range(dat.shape[0]):
    for c in range(dat.shape[1]):
        height = dat[r,c]

        up, down, left, right = np.flip(dat[:r,c]), dat[r+1:,c], np.flip(dat[r,:c]), dat[r,c+1:]
        dists = []
        for dir in up, down, left, right:
            dist = 0
            for tree in dir:
                dist += 1
                if tree >= height:
                    break
            dists.append(dist)
        score = prod(dists)
        if score > scenic_score:
            scenic_score = score
                
print(f"Max scenic score: {scenic_score}")
