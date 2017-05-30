import os
import queue


def get_subdir(path, ret_list):
    subdir_list = []
    try:
        dir_files = os.listdir(path)
    except:
        return subdir_list
    for each in dir_files:
        full_name = path + '/' + each
        if os.path.isdir(full_name):
            subdir_list.append(full_name + '/')
        if ~(full_name.find(".py") == -1):
            ret_list.append(full_name)
    return subdir_list


def solution(v):
    ret_list = []
    dir_queue = queue.Queue()
    dir_queue.put(v)
    while not dir_queue.empty():
        dir_path = dir_queue.get()
        subdir_path = get_subdir(dir_path, ret_list)
        for each in subdir_path:
            dir_queue.put(each)
    ret_list.sort()
    return ret_list


if __name__ == '__main__':
    v = input()
    output = solution(v)
    print(output)
