with open("input.txt") as f:
    dat = f.read()

def detect_marker(stream, marker_size):
    letters = [x for x in stream[:marker_size]]
    uniq = set(letters)
    ind = marker_size-1
    while len(uniq)<marker_size:
        if ind==len(stream)-1:
            return False
        ind += 1
        del letters[0]
        letters.append(stream[ind])
        uniq = set(letters)
    return(ind + 1)

print(detect_marker(dat, 4))
print(detect_marker(dat, 14))
