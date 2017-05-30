import os, queue

dir_queue = queue.Queue()

#initial state
path = input("Please input the search start path : ")
dir_queue.put(path)
all_dirs = []

def get_subdir(path):
    subdir_list = []
    try:
        dir_files = os.listdir(path)
    except:
        return subdir_list
    #delete file from list
    for each in dir_files:
        full_name = path + '/' + each
        if os.path.isdir(full_name):
            subdir_list.append(full_name + '/')
    return subdir_list


while not dir_queue.empty():
    dir_names = dir_queue.get() # pop first queue
    subdir_names = get_subdir(dir_names)

    all_dirs.append(dir_names)
    for each in subdir_names:
        dir_queue.put(each)

print(all_dirs)
