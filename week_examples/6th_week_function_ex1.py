# -*- coding: utf-8 -*-

import subprocess

def clear_screen():
    """화면을 지우는 함수 (Windows 환경)"""
    subprocess.run('cls', shell=True)

def print_menu_list():
    """메뉴를 출력하는 함수"""
    print("\n#### 메뉴 ####")
    menu = ["1. 자신의 이름 입력, 출력 코드", 
            "2. 자신의 학번 입력, 출력 코드", 
            "3. 애국가 1절 출력 코드", 
            "4. 고급 계산기 프로그램",
            "5. 도형의 넓이 계산기 프로그램",
            "6. 성적 구하기 프로그램",
            "7. 도형 그리기 프로그램",
            "8. 타이머 프로그램",
            "9. 자판기 프로그램"
            "10. 종료"]
    
    for i in menu:
        print(i)
    

def print_menu(select = 0):
    print("\n#### 메뉴 ####")
    print("1. 자신의 이름 입력, 출력 코드")
    print("2. 자신의 학번 입력, 출력 코드")
    print("3. 애국가 1절 출력 코드")
    print('4. 고급 계산기 프로그램')
    print('5. 도형의 넓이 계산기 프로그램')
    print('6. 성적 구하기 프로그램')
    print('7. 도형 그리기 프로그램')
    print('8. 타이머 프로그램')
    print("9. 종료")

    return input("메뉴를 선택하세요(1 ~ 9): ")

def main():
    """메인 함수"""
    while True:
        clear_screen()
        select = print_menu()
        #select = print_menu_list()

        if select == "1":
            # 이름 입력, 출력 코드
            pass
        elif select == "2":
            # 학번 입력, 출력 코드
            pass
        elif select == "3":
            # 애국가 1절 출력 코드
            pass
        elif select == "4":
            # 고급 계산기 프로그램
            pass
        elif select == "5":
            # 넓이 계산기 프로그램
            pass
        elif select == "6":
            # 성적 구하기 프로그램
            pass
        elif select == "7":
            # 도형 그리기 프로그램
            pass
        elif select == "8":
            # 타이머 프로그램
            pass
        elif select == "9":
            clear_screen()
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()      
    

