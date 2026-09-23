import subprocess
import time

def clear_display():
    """화면을 지우는 함수 (Windows 환경)"""
    subprocess.run('cls', shell=True)
    

def run_timer(set_timer = 10):
    
    print(f"{set_timer}초 시계 동작 시작!")
    time.sleep(2)
    
    # 1초부터 10초까지 1초 간격으로 출력
    for sec in range(1, set_timer):
        clear_display()
        print(f"현재 {sec}초 경과...")
        time.sleep(1)  # 1초 동안 프로그램 정지

    print("시간 종료!")

def run_time_bomb(setup_timer):
    
    print("===================================")
    time.sleep(2)

    # range(시작, 끝, 증감) -> 30부터 1까지 -1씩 감소
    for count in range(setup_timer, 0, -1):
        clear_display()
        print(f"💣 폭파까지 남은 시간: {count}초...")
        time.sleep(1)

    print("===================================")
    print("💥 💥 💥 펑! 폭탄이 터졌습니다! 💥 💥 💥")

def run_time_bomb_ms(setup_ms):
    print("===================================")
    time.sleep(2)

    # range(시작, 끝, 증감) -> 30부터 1까지 -1씩 감소
    for count in range(setup_ms*10, 0, -1):
        clear_display()
        print(f"💣 폭파까지 남은 시간: {count/10:.1f}초...")
        time.sleep(.1)

    print("===================================")
    print("💥 💥 💥 펑! 폭탄이 터졌습니다! 💥 💥 💥")


def menu_timer():
    print("\n#### 타이머 메뉴 ####")
    print("1. Set timer 코드")
    print("2. 시한폭탄 코드")
    print("3. 시한폭탄(밀리초) 출력 코드")

    sel = int(input('선택하세요: '))
    set_time = int(input('몇 초로 타이머를 맞출 까요?'))

    if sel == 1:
        run_timer(set_time)
    elif sel == 2:
        run_time_bomb(set_time)
    elif sel == 3:
        run_time_bomb_ms(set_time)
    else:
        print('잘 못 설정된 타이머 시간입니다.')

def main():
    clear_display()
    menu_timer()

    
if __name__ == '__main__':
    main()