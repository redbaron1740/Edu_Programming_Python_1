# -*- coding: utf-8 -*-
import subprocess

def clear_screen():
    """화면을 지우는 함수 (Windows 환경)"""
    subprocess.run('cls', shell=True)


# #예제1

def input_name():
    name = input('이름을 입력하세요:')
    print( f'당신의 이름은:{name}' )

def input_student_id():
    student_id = input('학번을 입력하세요:')
    print( f'당신의 학번은:{student_id}' )
    
def input_national_anthem():
    print('애국가 1절')
    print('동해물과 백두산이 마르고 닳도록')
    print('하느님이 보우하사 우리나라 만세')
    print('무궁화 삼천리 화려강산')
    print('대한사람 대한으로 길이 보전하세')
    
def input_simple_calculator():
    equation = input('수식을 입력하세요(예: 5 + 3):')
    result = 0

    if '+' in equation:
        x, y = equation.split('+')
        x = float(x)
        y = float(y)
        result = x + y
        
    elif '-' in equation:
        x, y = equation.split('-')
        x = float(x)
        y = float(y)
        result = x - y

    elif '*' in equation:
        x, y = equation.split('*')
        x = float(x)
        y = float(y)
        result = x * y
    
    elif '/' in equation:
        x, y = equation.split('/')
        x = float(x)
        y = float(y)
        result = x / y
        
    print( f'결과:{result}' )

def input_advanced_calculator():
    equation = input('수식을 입력하세요(예: (4.3*2.0) + (5.0/2.0) - 1.0):')
    result = eval(equation)
    print( f'계산 결과:{result}' )

def main():
    """메인 함수"""
    clear_screen()
    
    print("\n#### 메뉴 ####")
    print("1. 자신의 이름 입력, 출력 코드")
    print("2. 자신의 학번 입력, 출력 코드")
    print("3. 애국가 1절 출력 코드")
    print('4. 심플 계산기 프로그램')
    print('5. 고급 계산기 프로그램')
    
    select = int(input("메뉴를 선택하세요(1 ~ 5): "))

    if select == 1:
        input_name()
    elif select == 2:
        input_student_id()
    elif select == 3:
        input_national_anthem()
    elif select == 4:
        input_simple_calculator()
    elif select == 5:
        input_advanced_calculator()
    else:
        print("잘못된 선택입니다. 다시 입력해주세요.")

print("프로그램을 종료합니다.")

if __name__ == '__main__':
    main()
    
   