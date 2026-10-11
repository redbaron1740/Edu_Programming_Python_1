import json
import subprocess
from pathlib import Path


RECORD_DIR = Path(__file__).resolve().parent / 'save_record'
RECORD_FILE = RECORD_DIR / '2026_Politek_college_record.txt'


def save_student_records(student_list: list):
    RECORD_DIR.mkdir(parents=True, exist_ok=True)
    record_file = open(RECORD_FILE, 'w', encoding='utf-8')
    json.dump(student_list, record_file, ensure_ascii=False, indent=2)
    record_file.close()


def load_student_records():
    RECORD_DIR.mkdir(parents=True, exist_ok=True)
    if not RECORD_FILE.exists():
        save_student_records([])
        return []

    record_file = open(RECORD_FILE, 'r', encoding='utf-8')
    student_list = json.load(record_file)
    record_file.close()
    if not isinstance(student_list, list):
        raise ValueError('학생 기록 파일의 최상위 데이터는 목록이어야 합니다.')
    return student_list

def clear_screen():
    subprocess.run('cls',shell=True)
    
def create_student_info(student_info: dict):
    student_info['st_name']         =       input('학생의 이름을 입력하시오: ')
    student_info['st_id']           =   int(input('학생의 학번을 입력하시오: '))
    phone_num = input('학생의 핸드폰 번호를 입력하시오: ')
    if phone_num.isdigit() and len(phone_num) == 11:
        phone_num = f'{phone_num[:3]}-{phone_num[3:7]}-{phone_num[7:]}'
    student_info['st_phone_num'] = phone_num
    
    sub_sel = int(input('전공을 입력하세요(1:ECO마더팩토리, 2:AI모빌리티): '))
    if sub_sel == 1:
        student_info['class_']      = 'ECO마더팩토리'
    elif sub_sel == 2:
        student_info['class_']      = 'AI모빌리티'
   
def calculate_grade_subject_(student_info: dict):
    print('\n과목의 성적을 순서대로 입력하시오 \n')

    student_info['Korean']          = float(input('학생의 국어 성적을 입력하시오: '))
    student_info['English']         = float(input('학생의 영어 성적을 입력하시오: '))
    student_info['Math']            = float(input('학생의 수학 성적을 입력하시오: '))
    student_info['Social']          = float(input('학생의 사회 성적을 입력하시오: '))
    student_info['Science']         = float(input('학생의 과학 성적을 입력하시오: '))
    
    total = 0
    
    for subject in ('Korean', 'English', 'Math', 'Social', 'Science'):
        total += student_info[subject]
        
    student_info['Avg'] = total / 5.0
    
    avg = student_info['Avg']
    
    if avg >= 95 :
        student_info['grade'] = 'A+'
    elif avg >= 90 :
        student_info['grade'] = 'A'
    elif avg >= 85 :
        student_info['grade'] = 'B+'
    elif avg >= 80 :
        student_info['grade'] = 'B'
    elif avg >= 60 :
        student_info['grade'] = 'C'
    else:
        student_info['grade'] = 'F'
    

def add_student_info(student_list: list, student_info ):
    print('순서에 맞추어 데이터를 입력하세요')
    create_student_info(student_info)
    calculate_grade_subject_(student_info)

    student_list.append(student_info.copy())


def search_student_info(student_list: list, student_name: str):
    for student in student_list:
        if student['st_name'] == student_name:
            return student
    return None

def print_all_students_info(student_list: list):
    for index, student in enumerate(student_list):
        print(f'{index+1}. {student}\n')


def delete_student_info(student_list: list, student_name: str):
    student_info = search_student_info(student_list, student_name)
    if student_info is not None:
        student_list.remove(student_info)
    else: 
        print('입력하신 학생정보는 존재하지 않습니다.')
    
def print_menu_list():
    print()
    print('#'*4 + ' 학생 기록부 ' + '#'*4)    
    print('1. 학생 기록 카드 추가하기')
    print('2. 학생 기록 카드 삭제하기')
    print('3. 학생 기록 검색하기')
    print('4. 학생 기록 변경하기')
    print('5. 전체 학생 기록 출력하기')
    print('프로그램 종료 q')
    
    return input('입력 진행하시겠습니까? (1-5, q) ').lower()

def print_modifying_info(student_list: list):
    if not student_list:
        print('학생 기록이 없습니다.')
        return

    student_name = input('수정할 학생의 이름은 무엇입니까? ')
    student_info = search_student_info(student_list, student_name)
    if student_info is None:
        print('입력하신 학생정보는 존재하지 않습니다.')
        return

    print(f"{student_info['st_name']}의 정보 중 어느 내용을 수정하시겠습니까?")
    print('1. 이름')
    print('2. 학번')
    print('3. 전화번호')
    print('4. 과정')
    print('5. 성적')
    sel = input('선택하시오(1-5, 상위메뉴는 엔터를 입력하시오): ').lower()

    if sel == '':
        return
    if sel == '1':
        student_info['st_name'] = input('이름을 수정하세요: ')
    elif sel == '2':
        try:
            student_info['st_id'] = int(input('학번을 수정하세요: '))
        except ValueError:
            print('학번은 숫자로 입력해야 합니다.')
            return
    elif sel == '3':
        phone_num = input('전화번호를 수정하세요: ')
        if phone_num.isdigit() and len(phone_num) == 11:
            phone_num = f'{phone_num[:3]}-{phone_num[3:7]}-{phone_num[7:]}'
        student_info['st_phone_num'] = phone_num
    elif sel == '4':
        try:
            sel_class_ = int(input('전공을 입력하세요(1:ECO마더팩토리, 2:AI모빌리티): '))
        except ValueError:
            print('전공은 1 또는 2로 입력해야 합니다.')
            return
        if sel_class_ == 1:
            student_info['class_'] = 'ECO마더팩토리'
        elif sel_class_ == 2:
            student_info['class_'] = 'AI모빌리티'
        else:
            print('전공은 1 또는 2로 입력해야 합니다.')
            return
    elif sel == '5':
        calculate_grade_subject_(student_info)
    else:
        print('1부터 5까지 선택해야 합니다.')
        return

    print(f'수정된 학생 정보: {student_info}')

    
def main():
    A_class_students_info = load_student_records()
    student_info = {
        'st_name': '',      #학생 이름
        'st_id':0,          #학생의 학번
        'st_phone_num':'',  #학생의 핸드폰 번호
        'class_':    '',
        'Korean':   .0,
        'English':  .0,
        'Math':     .0,
        'Social':   .0,
        'Science':  .0,
        'Avg':      .0,
        'grade': ''
    }
    
    isRunning = True

    
    while isRunning:
        
        clear_screen()
        
        sel = print_menu_list()
               
        if sel == '1':
            clear_screen()
            add_student_info(A_class_students_info,student_info)
            save_student_records(A_class_students_info)
            print(f'\n\n기록된 학생의 정보: {student_info}\n') 
            input('상위 메뉴로 이동하려면 아무키나 누르시오.')           

        elif sel == '2':
            clear_screen()
            delete_student_info(A_class_students_info,student_name=input('삭제할 학생의 이름을 입력하시오: '))
            save_student_records(A_class_students_info)
            input('상위 메뉴로 이동하려면 아무키나 누르시오.')

            
        elif sel == '3':
            clear_screen()
            student_name = input('검색할 이름을 입력하시오: ')                        
            student = search_student_info(A_class_students_info, student_name)
            
            if student is None:
                print('해당 학번의 학생 기록을 찾을 수 없습니다.')
            else:
                print(f'검색 결과: {student}')
            input('상위 메뉴로 이동하려면 아무키나 누르시오.')

        elif sel == '4':
            clear_screen()
            print_modifying_info(A_class_students_info)
            save_student_records(A_class_students_info)
            input('상위 메뉴로 이동하려면 아무키나 누르시오.')

        elif sel == '5':
            clear_screen()
            if A_class_students_info is not None:
                print_all_students_info(A_class_students_info)
            else:
                print('학생 기록이 없습니다.')
            input('상위 메뉴로 이동하려면 아무키나 누르시오.')

        elif sel == 'q':
            isRunning = False
            print('프로그램 종료합니다.')
        else:
            input('잘못 선택하였습니다. 다시 선택하시려면 아무키나 누르시오.')
    save_student_records(A_class_students_info)
        
    
if __name__ == '__main__':
    main()