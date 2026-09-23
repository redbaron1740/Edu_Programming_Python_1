import subprocess

def clear_screen():
    """화면을 지우는 함수 (Windows 환경)"""
    subprocess.run('cls', shell=True)
    
    
def print_menu_area():
    print("\n#### 도형 넓이 구하기 프로그램 ####\n")
    print("1. 사각형 넓이 계산기")
    print("2. 삼각형 넓이 계산기")
    print("3. 원 넓이 계산기")
    print("4. 마름모 넓이 계산기\n")

    return int(input("메뉴를 선택하세요(1 ~ 4): "))
    

# 도형 넓이 구하기 프로그램
def calculate_area(select = 1):
    """도형 넓이 구하기 프로그램"""
    clear_screen()

    if select == 1:
        width = float(input("사각형의 가로 길이를 입력하세요: "))
        height = float(input("사각형의 세로 길이를 입력하세요: "))
        area = width * height
        print(f"사각형의 넓이는: {area:.2f}")

    elif select == 2:
        base = float(input("삼각형의 밑변 길이를 입력하세요: "))
        height = float(input("삼각형의 높이를 입력하세요: "))
        area = (base * height) / 2
        print(f"삼각형의 넓이는: {area:.2f}")

    elif select == 3:
        radius = float(input("원의 반지름을 입력하세요: "))
        area = 3.14159 * (radius ** 2)
        print(f"원의 넓이는: {area:.2f}")

    elif select == 4:
        diagonal1 = float(input("마름모의 첫 번째 대각선 길이를 입력하세요: "))
        diagonal2 = float(input("마름모의 두 번째 대각선 길이를 입력하세요: "))
        area = (diagonal1 * diagonal2) / 2
        print(f"마름모의 넓이는: {area:.2f}")

    else:
        print("잘못된 메뉴를 선택하였습니다.")

    
def main():
    """메인 함수"""
    clear_screen()
    print("\n#### 메뉴 ####")
    print('1. 도형 넓이 구하기 프로그램')
    
    select = int(input("메뉴를 선택하세요(1): "))
    
    if select == 1:
        calculate_area(print_menu_area())

if __name__ == "__main__":
    main()