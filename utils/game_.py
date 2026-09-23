# -*- coding: utf-8 -*-


#  본 코드는 시간 안에 특정 문자를 찾아 빠른 시간 안에 
#  시간을 멈추는 것이다.
#  필요 기능
# 
# # +-----------------------------+-----------------+
# # |         Function            |       Library   |
# # |          time elapsed       |        time     |
# # |       Gain keyboard data    |       mscrvt    |
# # |       command window        |     subprocess  |
# # |       randomizing           |     random      |
# # +-----------------------------+-----------------+

import time
import msvcrt          
import subprocess
import random
import string

#REAL_DEFUSE_KEY = random.choice(string.ascii_lowercase)

def clear_display():
    subprocess.run('cls',shell=True)
    
    
def get_defuse_key():
    return random.choice(string.ascii_lowercase)

def operating_task(total_time):
    defuse_key = get_defuse_key()
    is_defused = False
    start_time = time.time()
    operating_count = 0
    
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = total_time - elapsed_time
        current_str = '시한폭탄 작동 중'+'.'*operating_count
        
        if remaining_time <= 0:
            break
            
        if operating_count > 5:
            operating_count = 0    
            
        clear_display()
        print("==================================================")
        print("       ⚠️  보안 등급: 시한폭탄 장전됨   ⚠️           ")
        print("==================================================")
        print(f"  💣 폭파까지 남은 시간: {remaining_time:.1f}초         ")
        print(f"  🔑       해체 키를 누르세요!                     ")
        print("==================================================")
        print(f"  💬 [System]: {current_str}                  ")
        print("==================================================")
        
        #키보드 입력 감지 기능
        if msvcrt.kbhit():
            char = msvcrt.getch().decode('utf-8').lower()
            
            if char == defuse_key:
                # 헤체 코드 입력됨
                is_defused = True
                break
            else:
                start_time -= 1.5  # 틀린 코드 입력 시 시간 차감 (1.5초)
                
        operating_count += 1
        time.sleep(0.1)
        
    print("==================================================")
    
    if is_defused == True:
        print("🎉 [SUCCESS] 해제 코드 설정, 폭탄 헤체됨 !!!!")
    else:
        print("      💥 💥 💥 [BOOM] !!!! 💥 💥 💥       ")
    print("==================================================")
            
    

def main():
    total_time = 100
    
    clear_display()
    print('시한폭탄 해체 게임입니다. 해체 코드를 넣으시오')
    operating_task(total_time)
       
        
    
if __name__ == '__main__':
    main()