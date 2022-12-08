big_size = 0

class Directory:
    def __init__(self, parent = None):
        self.files = {}
        self.subdirs = {}
        self.parent = parent
    
    def get_size(self):
        global big_size
        size = 0
        for file in self.files:
            #print(size, self.files, file)
            file_size = self.files[file]
            print("*", file, file_size)
            size += file_size
        for dir in self.subdirs:
            #print(size, self.subdirs, dir)
            subdir_size = self.subdirs[dir].get_size()
            print("#", dir, subdir_size)
            with open('subdirs', 'a+') as fp:
                fp.write("# " + dir + " " + str(subdir_size) + '\n')
            size += subdir_size
            if subdir_size <= 100000:
                big_size += subdir_size
        return size
    
    def add_dir(self, name):
        self.subdirs[name] = Directory(self)
        return self.subdirs[name]
    
    def add_file(self, name, size):
        self.files[name] = size

    def dir_exists(self, name):
        return name in self.subdirs
    
    def list_dirs(self):
        print(self.subdirs)
    
    def get_dirs(self):
        return self.subdirs

    def list_files(self):
        print(self.files)
    
    def get_files(self):
        return self.files

    def get_parent(self):
        if self.parent == None: return self
        return self.parent

with open('input', 'r') as fp:
    history = fp.readlines()[::-1]

cwd = Directory()
root = cwd.get_parent()

while history:
    line = history.pop().strip()

    if line.startswith('$'): # command
        line = line[2:]
        if line == 'ls':
            files_to_add = []
            while history and not history[-1].startswith('$'): files_to_add.append(history.pop().strip())
            #print(files_to_add)
            for file in files_to_add:
                if file.startswith('dir'):
                    cwd.add_dir(file.split(' ')[1])
                else:
                    size, name = file.split(' ')
                    cwd.add_file(name, int(size))
        elif line.startswith('cd'):
            command, operand = line.split(' ')
            #print(command, operand)
            if operand == '/': cwd = root
            elif operand == '..': cwd = cwd.get_parent()
            elif cwd.dir_exists(operand): cwd = cwd.get_dirs()[operand]
            else: cwd = cwd.add_dir(operand)
        else: 
            print('something is very wrong')

print(root.get_size())
print(big_size)
