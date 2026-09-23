# -*- coding: utf-8 -*-
import subprocess
from utils.make_shape import make_shape

subprocess.run('cls', shell=True)

print('####### 메뉴 ######\n\n')

print('1. 계산기 프로그램')
print('2. 넓이 계산기 프로그램')
print('3. 별 모양 그리기 프로그램\n\n')

메뉴_고름 = input('메뉴를 선택하세요(1 ~ 3):')

print( f'\n선택된 메뉴:{메뉴_고름}' )

if 메뉴_고름 == '1':
    공식 = input('공식을 입력하세요(예: (4.3*2.0) + (5.0/2.0) - 1.0):')
    try:
        결과 = eval(공식)
        print(f'계산 결과:{결과}')
    except Exception as 오류:
        print(f'올바른 수식을 입력하세요. 오류: {오류}')

elif 메뉴_고름 == '2':
    subprocess.run('cls', shell=True)
    print('\n####### 넓이 계산기 ######\n\n')
    print('1. 사각형 넓이 계산기')
    print('2. 삼각형 넓이 계산기')
    print('3. 원 넓이 계산기\n\n')

    넓이_계산기_선택 = input('넓이 계산기를 선택하세요(1 ~ 3):')

    if 넓이_계산기_선택 == '1':
        가로 = float(input('사각형의 가로 길이를 입력하세요:'))
        세로 = float(input('사각형의 세로 길이를 입력하세요:'))
        넓이 = 가로 * 세로
        print(f'사각형의 넓이는: {넓이}')

    elif 넓이_계산기_선택 == '2':
        밑변 = float(input('삼각형의 밑변 길이를 입력하세요:'))
        높이 = float(input('삼각형의 높이를 입력하세요:'))
        넓이 = (밑변 * 높이) / 2
        print(f'삼각형의 넓이는: {넓이}')

    elif 넓이_계산기_선택 == '3':
        반지름 = float(input('원의 반지름을 입력하세요:'))
        넓이 = 3.14159 * (반지름 ** 2)
        print(f'원의 넓이는: {넓이}')

    else:
        print('잘못된 메뉴를 선택하였습니다.')    

elif 메뉴_고름 == '3':
    subprocess.run('cls', shell=True)

    print('\n####### 별 모양 그리기 ######\n\n')
    print('1. 삼각형')
    print('2. 사각형')
    print('3. 마름모')
    print('4. 다이아몬드')
    print('5. 원\n')

    도형_선택 = input('그릴 도형을 선택하세요(1 ~ 5):')
    
    make_shape(도형_선택)
    
else :
    print('잘못된 메뉴를 선택하였습니다.')
    
print('\n프로그램을 종료합니다.')
