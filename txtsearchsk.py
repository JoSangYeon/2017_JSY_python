# 함수들을 불러옵니다
import os, queue

#하위 디렉터리 찾는 함수
def get_subdir( path, ret_list ) : #함수 이름 선언
    subdir_list = [] #하위 디렉터리 리스트
    try : #파이썬이 한번 실행해봄
        dir_files = os.listdir(path) #'path' 디렉터리에 대하여 파일과 하위디렉터리를 검색
    except : #오류 발생하면, 하위 디렉터리를 다시 넣을 때 파일을 처리하는 부분같아요.
        return subdir_list
    for each in dir_files : #디렉터리와 파일들 모두 있는 리스트
    #풀네임 : 바탕화면/사진이 아니라 바탕화면/사진/ >> 하위 디렉터리 찾을 때 프로그램이 알아볼 수 있게 해 주는 것 같아요
        full_name = path + '/' + each
        #디렉터리가 맞으면!
        if os.path.isdir(full_name) :
            subdir_list.append(full_name + '/')
        #디렉터리가 아니면 ? >> 파일이니까 파일 이름에서 txt를 찾습니다!
    return subdir_list # 하위 디렉터리 리턴

 def solution( v ) :
    ret_list = []
    dir_queue = queue.Queue()
    dir_queue.put(v)
    while not dir_queue.empty() :
        dir_path = dir_queue.get()
        subdir_path = get_subdir(dir_path, ret_list)
        for each in subdir_path :
            dir_queue.put(each)
    ret_list.sort()
    return ret_list

if __name__ == '__main__' :
    v = input()
    output = solution(v)
    print(output)
