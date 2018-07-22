import os
import sys
import time

# set max recursive
sys.setrecursionlimit(1000000000)

# directory
path = sys.argv[1]
print("directory：" + path)

# file number
index = 1

def rename(path):
    global index
    filelist = os.listdir(path)
    for file in filelist:
        # print(file)
        old_name = file
        old_dir = os.path.join(path, file)
        if os.path.isdir(old_dir):  # directory
            rename(old_dir)
        file_name = os.path.splitext(file) # split file to file and file name
        # file suffix
        file_name_2 = file_name[1].lower()
        # print(file_name_1)
        # print(file_name_2)

        # exist '#n#' hidden mode, change file suffix, remove '#n#'
        # not exist '#n#', remove '#n#'
        if "#n#" in file_name_2:  # check '#n#'
            file_name_2 = file_name_2.replace("#n#", "") # replace '#n#' to ''
        else:
            file_name_2 = file_name_2 + "#n#"
        
        new_dir = os.path.join(path, str(index) + file_name_2)
        try :
            os.rename(old_dir, new_dir)
            print(old_name + "    replaced to    " + str(index) + file_name_2)
            index += 1
        except PermissionError as pe:
            print(pe)


rename(path)