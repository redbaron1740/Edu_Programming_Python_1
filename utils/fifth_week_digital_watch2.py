import curses
import time

# 0~9 및 콜론(:)의 7-세그먼트 아트 (높이 5줄)
digits = [
    [" ### ", "#   #", "#   #", "#   #", " ### "],  # 0
    ["  #  ", " ##  ", "  #  ", "  #  ", " ### "],  # 1
    [" ### ", "    #", " ### ", "#    ", " ### "],  # 2
    [" ### ", "    #", " ### ", "    #", " ### "],  # 3
    ["#   #", "#   #", " ####", "    #", "    #"],  # 4
    ["#### ", "#    ", "#### ", "    #", "#### "],  # 5
    [" ### ", "#    ", "#### ", "#   #", " ### "],  # 6
    ["#####", "    #", "   # ", "  #  ", " #   "],  # 7
    [" ### ", "#   #", " ### ", "#   #", " ### "],  # 8
    [" ### ", "#   #", " ####", "    #", " ### "],  # 9
    ["     ", "  #  ", "     ", "  #  ", "     "]   # : (인덱스 10)
]

def draw_clock(stdscr):
    # 1. 터미널 설정 (커서 숨기기 및 키 입력 딜레이 설정)
    curses.curs_set(0)
    stdscr.nodelay(True)  # getch() 실행 시 블로킹 없이 바로 넘어가도록 설정
    stdscr.clear()

    while True:
        # 화면 깨끗이 지우기
        #stdscr.erase()
        stdscr.clear()

        # 현재 시간 가져오기
        time_str = time.strftime("%H:%M:%S")

        # 헤더 출력
        stdscr.addstr(1, 2, "==================================================")
        stdscr.addstr(2, 2, f"            현재 시각: {time_str}")
        stdscr.addstr(3, 2, "==================================================")

        # 7-세그먼트 디지털 시계 그려주기 (4번째 줄부터 출력)
        start_y = 5
        for row in range(5):
            line = ""
            for char in time_str:
                # idx = 10 if char == ":" else int(char)
                
                if char == ":":
                    idx = 10
                else:
                    idx = int(char)

                line += digits[idx][row] + "  "
            
            # curses는 print 대신 addstr을 사용합니다.
            stdscr.addstr(start_y + row, 2, line)

        # 푸터 출력
        stdscr.addstr(11, 2, "==================================================")
        stdscr.addstr(12, 2, "(종료하려면 'q' 키 또는 Ctrl+C를 누르세요)")

        # 화면 갱신
        stdscr.refresh()

        # 종료 키('q') 입력 감지
        key = stdscr.getch()
        if key == ord('q') or key == ord('Q'):
            break

        # 0.2초 간격으로 화면 업데이트 (반응성 향상)
        time.sleep(0.2)

def display_digital_clock():
    try:
        curses.wrapper(draw_clock)
    except KeyboardInterrupt:
        pass

def main():
    # curses.wrapper가 터미널 초기화 및 복구를 안전하게 처리합니다.
    display_digital_clock()
    
    
if __name__ == '__main__':
    main()