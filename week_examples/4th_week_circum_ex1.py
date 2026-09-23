# -*- coding: utf-8 -*-

import subprocess

def make_shape(select = 1):
    
    print('\n\n')

    if select == 1:
        ## 1. right triangle
        for i in range(1, 6):
            print("*" * i)
    elif select == 2:
        ## 2. inverted right triangle
        for i in range(5, 0, -1):
            print("*" * i)
    
    elif select == 3:
        ## 3. isosceles triangle
        for i in range(1, 6):
            print(" " * (5 - i) + "*" * (2 * i - 1))
            
    elif select == 4:
        ## 4. inverted isosceles triangle
        for i in range(5, 0, -1):
            print(" " * (5 - i) + "*" * (2 * i - 1))
            
    elif select == 5:
        ## 5. Rectangle
        for i in range(5):
            print("*" * 10)
    elif select == 6:
        ## 6. Square
        for i in range(5):
            print("*" * 5)
    elif select == 7:
        ## 7. Diamond
        for i in range(1, 6):
            print(" " * (5 - i) + "*" * (2 * i - 1))
        for i in range(4, 0, -1):
            print(" " * (5 - i) + "*" * (2 * i - 1))
    else:
        print('잘못 선택하셨습니다.')
            
    print('\n\n')

    
def main():
    """화면을 지우는 함수 (Windows 환경)"""
    subprocess.run('cls', shell=True)

    print("\n#### 메뉴 ####")
    print("1. 직각삼각형 출력 코드")
    print("2. 역직각삼각형 출력 코드")
    print("3. 이등변삼각형 출력 코드")
    print('4. 역이등변삼각형 출력 프로그램')
    print('5. 직사각형 출력 프로그램')
    print('6. 정사각형 출력 프로그램')
    print('7. 마름모 출력 프로그램')
    print('8. 메인 메뉴로 이동\n\n')
    
    make_shape(int(input('선택하세요.(1 - 8)')))
    
if __name__ == '__main__':
    main()