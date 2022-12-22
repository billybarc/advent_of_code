import numpy as np # so I can do coordinate addition

with open("input.txt") as f:
    dat = f.read()

# x,y
h_coord = np.array([0,0])
t_coord =np.array([0,0])

# letter to coord adjustment dict
dirs = {"R": [1,0],
        "RU": [1,1],
        "U": [0,1],
        "LU": [-1,1],
        "L": [-1,0],
        "LD": [-1,-1],
        "D": [0,-1],
        "RD": [1,-1],
        "N": [0,0]}

# keys are tuples of head minus tail coords
# values are directions for tail to go
chase_dir = {(0,0): "N",
             (2,0): "R",
             (2,1): "RU",
             (2,2): "RU",
             (1,2): "RU",
             (0,2): "U",
             (-1,2): "LU",
             (-2,2): "LU",
             (-2,1): "LU",
             (-2,0): "L",
             (-2,-1): "LD",
             (-2,-2): "LD",
             (-1,-2): "LD",
             (0,-2): "D",
             (1,-2): "RD",
             (2,-2): "RD",
             (2,-1): "RD",
             (1,0): "N",
             (0,1): "N",
             (-1,0): "N",
             (0,-1): "N",
             (1,1): "N",
             (-1,1): "N",
             (-1,-1): "N",
             (1,-1): "N"}

coords = {tuple(t_coord)}
for l in dat.splitlines():
    dir, mag = l.split(" ")
    for i in range(int(mag)):
        h_coord = h_coord + dirs[dir]
        diff = tuple(h_coord - t_coord)
        t_move_dir = chase_dir[diff]
        t_move_dir_coords = dirs[t_move_dir]
        t_coord = t_coord + t_move_dir_coords
        coords.add(tuple(t_coord))

print(f"# of unique coordinates: {len(coords)}")

# part 2
coords = np.array(list(np.array([0,0]) for i in range(10)))
t_coords = {tuple(coords[-1])}
for l in dat.splitlines():
    dir, mag = l.split(" ")
    for i in range(int(mag)):
        coords[0] = coords[0] + dirs[dir]
        for j in range(1,len(coords)):
            diff = tuple(coords[j-1] - coords[j])
            t_move_dir = chase_dir[diff]
            t_move_dir_coords = dirs[t_move_dir]
            coords[j] = coords[j] + t_move_dir_coords
            if j==len(coords)-1:
                t_coords.add(tuple(coords[j]))

print(f"# of unique coordinates: {len(t_coords)}")
