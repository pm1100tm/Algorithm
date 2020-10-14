def get_file_path():
    pathlist = []
    path = os.getcwd() + "/quiz/codingDojang/Python-Algorithm/002_source_code_file"
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                pathlist.append(root + "/" + file)
            else: pass

    return pathlist

def file_read_write():
    pathlist = get_file_path()
    print(pathlist)
    for path in pathlist:
        try:
            new_lines = []
            with open(path, "r") as f:
                lines = f.readlines()
                for line in lines:
                    new_lines.append(line.replace("\t", " "*4))

            with open(path, "w") as f:
                f.writelines(new_lines)

        except Exception as e:
            print(e)

file_read_write()