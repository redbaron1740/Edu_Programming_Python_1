import subprocess

A_class_students_info = []


def clear_screen():
    subprocess.run('cls',shell=True)
    

def add_student_info(student_list: list, student_info ):
    student_list.append(student_info)

    
def main():
    student_info = {
        'st_name': '',      #학생 이름
        'st_id':0,          #학생의 학번
        'st_phone_num':'',  #학생의 핸드폰 번호
        'class_year': 0,
        'Korean':   .0,
        'English':  .0,
        'Math':     .0,
        'Social':   .0,
        'Science':  .0,
        'Avg':      .0,
        'archive': ''
    }
    print('학생기록카드입니다.')
    
    isRunning = True

    
    while isRunning:
        
        clear_screen()
        sel = input('입력 진행하시겠습니까? (y or n, p: print info)   ').lower()
               
        if sel == 'y':
            print('순서에 맞추어 데이터를 입력하세요')
            
            student_info['st_name']         =       input('학생의 이름을 입력하시오: ')
            student_info['st_id']           =   int(input('학생의 학번을 입력하시오: '))
            student_info['st_phone_num']    =       input('학생의 핸드폰 번호를 입력하시오: ')
            
            print('\n성적 입력 순서 \n')
            student_info['class_year']      =       input('금년 학년을 입력하세요: ')
        
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
                student_info['archive'] = 'A+'
            elif avg >= 90 :
                student_info['archive'] = 'A'
            elif avg >= 85 :
                student_info['archive'] = 'B+'
            elif avg >= 80 :
                student_info['archive'] = 'B'
            elif avg >= 60 :
                student_info['archive'] = 'C'
            else:
                student_info['archive'] = 'F'
            
            add_student_info(A_class_students_info,student_info)

            print(f'기록된 학생의 정보: {student_info}')
            
            
        elif sel == 'n':
            isRunning = False
        elif sel == 'p':
            for index, student in enumerate(A_class_students_info):
                print(f'{index+1}. {student}')
                
            input('상위 메뉴로 넘어가기 위해 임의의 키를 누르세요')

    
    
        
    
if __name__ == '__main__':
    main()