import time
import json
import subprocess
from datetime import datetime 

# =================================================
# [1] 데이터 조작 함수 (find, append, insert, sort)
# =================================================

def find_data(data: dict, name: str) -> list:
    """이름(key: 'name')으로 학생정보 검색 함수"""
    result = []
    
    for class_name, student_list in data.items():
        for student in student_list:
            if student.get('name') == name:
                item = student.copy()
                item['class_name'] = class_name
                result.append(item)
    return result

def append_data(data: dict, class_name: str, name: str, students_id: int, phone_number: str):
    if class_name not in data:
        data[class_name] = []
        
    new_student = {
        "name": name,
        "student_id": students_id,
        "phone_num": phone_number
    }
    data[class_name].append(new_student)
    
def sort_data(data: dict) -> dict:
    """반별 학생 목록을 이름 (한글/알파벳) 가나다 순으로 정렬하는 함수"""
    sorted_data = {}
    for class_name, student_list in data.items():
        sorted_data[class_name] = sorted(student_list, key=lambda x: x["name"])
        
    return sorted_data
        

def clear_screen():
    subprocess.run('cls',shell=True)
    
#def generate_timestamp_filename(prefix: str = "students_info", extenion: str = "json") -> str:
#def create_file(file_path: str, data: dict):
#def delete_file(file_path: str):
#def read_file(file_path: str) -> dict:
#def save_file(file_path, data: dict, mode: str = "overwrite"):


def main():
    """초기 데이터 선언 및 초기화"""
    classroom_data = {
        "A반": [
            {"name":'admin', "student_id": 2611111, "phone_num": "010-1111-1111"},
            {"name":'unknown', "student_id": 0, "phone_num": "010-0000-0000"}
        ],
        "B반":[
            {"name":'unknown', "student_id": 0, "phone_num": "010-0000-0000"}
        ]
    }
    
    print('--- 학생 기록부 메뉴 ---')
    print('- 1. 데이터 추가 (Append) ')
    print('- 2. 학생 검색 (Find)')
    print('- 3. 전체 데이터 출력')
    choice_ = int(input('선택하시오(1-3) '))
    
    if choice_ == 1:
        isRunning = True
        while isRunning:                
            print('--- 학생 데이터 추가 메뉴 ---')
            data_class_ = input('학생의 반을 고르시오 (A반: A, B반: B): ').upper()
            data_name_ = input('학생의 이름을 입력하시오: ')
            data_id_ = int(input('학생의 아이디를 입력하시오: '))
            data_phone_ = input('학생의 전화번호를 입력하시오: ')
        
            if input('입력된 데이터가 확실합니까? yes(y) or 불확실(anykey))').lower() == 'y':
                append_data(classroom_data, data_class_, data_name_, data_id_, data_phone_)
            else:
                if input('재입력하시겠습니까? 확실(y) or 종료(anykey)').lower() == 'y':
                    isRunning = True
                else:
                    isRunning = False                    
                    


if __name__ == '__main__':
    main()

    