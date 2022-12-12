class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name}: {self.size}"

    def __repr__(self):
        return self.__str__()

class Folder:
    def __init__(self, name: str, parent: 'Folder' = None):
        self.name = name
        if self.name!="/" and parent is None:
            return ValueError("Non-root folders cannot have a None parent.")
        else:
            self.parent = parent
        self.contents = []

    def add_file(self, name, size):
        self.contents.append(File(name, size))

    def add_subfolder(self, folder: 'Folder'):
        self.contents.append(folder)

    def __str__(self):
        return f"""name: {self.name}
contents:
{self.contents}"""

    def __repr__(self):
        return self.__str__()

    def get_size(self, size = 0):
        if len(self.contents)==0:
            return size
        for x in self.contents:
            if isinstance(x, Folder):
                size = x.get_size(size)
            else:
                size += x.size
        return size

with open("input.txt") as f:
    dat = f.read().splitlines()

current_folder = None

for idx,l in enumerate(dat):
    tokens = l.split()
    if tokens[0]=="$":
        match tokens[1]:
            case "cd":
                arg = tokens[2]
                if arg=="..":
                    current_folder = current_folder.parent
                elif arg=="/":
                    if current_folder is None:
                        # initializing tree
                        current_folder = Folder("/")
                    else:
                        # climbing tree back to top
                        while current_folder.name!="/":
                            current_folder = current_folder.parent
                else:
                    if not arg in [x.name for x in current_folder.contents if isinstance(x,Folder)]:
                        current_folder.add_subfolder(arg, current_folder)
                    idx = 0
                    for x in current_folder.contents:
                        if x.name == arg:
                            break
                        idx += 1
                    current_folder = current_folder.contents[idx]
            case "ls":
                continue
    # if not a command (only cd or ls),
    # ls output
    elif tokens[0]=="dir":
        current_folder.add_subfolder(Folder(name = tokens[1], parent = current_folder))
    else:
        current_folder.add_file(tokens[1], int(tokens[0]))

def print_structure(f: 'Folder', ind = 0):
    print(" "*ind +"d " + f.name+" "+str(f.get_size())+" "+str(int(ind / 2)))
    for x in f.contents:
        if isinstance(x, Folder):
            print_structure(x, ind + 2)
        else:
            print(" "*(ind+2) + "f " + x.name + " " + str(x.size))

# go back to top
while (current_folder.name != "/"):
    current_folder = current_folder.parent

#print_structure(current_folder)

total_space = 70000000
min_space = 30000000
current_used = current_folder.get_size()
avail_space = total_space - current_used
needed_space = min_space - avail_space

size_sum = 0
min_size = 999999999
def extract_size(f: 'Folder'):
    global size_sum
    global min_size

    f_size = f.get_size()
    if f_size<=100000:
        size_sum += f_size
    if f_size >= needed_space and f_size < min_size:
        min_size = f_size
    for x in f.contents:
        if isinstance(x, Folder):
            extract_size(x)

extract_size(current_folder)
print(size_sum)
print(min_size)
