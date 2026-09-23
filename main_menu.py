import subprocess
import time
from utils.second_week import input_name, input_student_id, input_national_anthem, input_simple_calculator, input_advanced_calculator
from utils.third_week import print_menu_area, calculate_area
from utils.fourth_week import print_menu_shape, make_shape
from utils.fourth_week2 import menu_timer
from utils.fifth_week_digital_watch2 import display_digital_clock
from utils.game_ import operating_task

def clear_screen():
    """화면을 지우는 함수 (Windows 환경)"""
    subprocess.run('cls', shell=True)
    
def print_menu():
    print("\n#### 메뉴 ####")
    print("1. 자신의 이름 입력, 출력 코드")
    print("2. 자신의 학번 입력, 출력 코드")
    print("3. 애국가 1절 출력 코드")
    print('4. 심플 계산기 프로그램')
    print('5. 고급 계산기 프로그램')
    print('6. 도형의 넓이 구하기 프로그램')
    print('7. 도형 그리기 프로그램')
    print('8. 타이머 프로그램')
    print('9. 디지털 시계 프로그램')
    print('10.Game/ 폭탄 해체 프로그램')
    print('11. 프로그램 종료')
    
    return int(input("메뉴를 선택하세요(1 ~ 10): "))


def main():
    
    bIsRun = True
    
    while bIsRun:
        clear_screen()
        select = print_menu()
        
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
        elif select == 6:
            calculate_area(print_menu_area())
        elif select == 7:
            make_shape(print_menu_shape())
        elif select == 8:
            menu_timer()
        elif select == 9:
            display_digital_clock()
        elif select == 10:
            setup_time = 100 # 100sec
            operating_task(setup_time)
        elif select == 11:
            print(' 프로그램을 종료합니다.')    
            bIsRun = False
        else:
            print('잘못된 번호를 입력하셨습니다.')
            
        time.sleep(1)

            
if __name__ == '__main__':
    main()
    
   