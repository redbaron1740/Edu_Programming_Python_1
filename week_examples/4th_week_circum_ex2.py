
# 예제 1
# import time

# print("10초 시계 동작 시작!")

# # 1초부터 10초까지 1초 간격으로 출력
# for sec in range(1, 11):
#     print(f"현재 {sec}초 경과...")
#     time.sleep(1)  # 1초 동안 프로그램 정지

# print("시간 종료!")




# 예제 2
### 시한폭탄 설정 프로그램
# import time

# 타이머설정 = int(input("⚠️ 시한폭탄을 몇초 설정할꺼요? (몇 1~100초)"))
# print("===================================")

# # range(시작, 끝, 증감) -> 30부터 1까지 -1씩 감소
# for count in range(타이머설정, 0, -1):
#     print(f"💣 폭파까지 남은 시간: {count}초...")
#     time.sleep(1)

# print("===================================")
# print("💥 💥 💥 펑! 폭탄이 터졌습니다! 💥 💥 💥")





# 예제 3    
# 시한폭탄 설정과 해제 프로그램 
# import time
# import subprocess
# import msvcrt  # Windows 전용 키보드 입력 모듈

# # 해제 비밀키 설정 ('q' 키)
# DEFUSE_KEY = 'q'

# total_seconds = 30
# start_time = time.time()
# is_defused = False

# print("⚠️ 시한폭탄이 활성화되었습니다!")
# print(f"💣 폭파 방지 해제 키: [{DEFUSE_KEY.upper()}] 키를 누르세요.\n")
# time.sleep(2)

# while True:
#     # 1. 경과 시간 및 남은 시간 계산
#     elapsed = time.time() - start_time
#     remaining = total_seconds - elapsed
    
#     # 2. 남은 시간이 0초 이하가 되면 폭파
#     if remaining <= 0:
#         break
    
#     # 3. 화면 갱신 및 남은 시간 출력 (소수점 1자리 표시)
#     subprocess.run('cls', shell=True)
#     print("===================================")
#     print(f"💣 폭파까지 남은 시간: {remaining:.1f}초")
#     print(f"🔑 해제 키: [{DEFUSE_KEY.upper()}] 키를 누르세요!")
#     print("===================================")
    
#     # 4. 실시간 키보드 입력 감지
#     if msvcrt.kbhit():  # 키보드 입력이 들어왔는지 확인
#         key = msvcrt.getch().decode('utf-8').lower()  # 입력된 키 확인
#         if key == DEFUSE_KEY:
#             is_defused = True
#             break  # 반복문 탈출!
            
#     # 0.1초 단위로 루프를 돌며 실시간 감지
#     time.sleep(0.1)

# # --- 결과 출력 ---
# subprocess.run('cls', shell=True)
# print("===================================")
# if is_defused:
#     print("🎉 [SUCCESS] 폭탄 해제 성공!")
#     print("디퓨즈 키가 정확히 입력되었습니다. 도시가 안전합니다!")
# else:
#     print("💥 💥 💥 [BOOM] 펑! 폭탄이 터졌습니다! 💥 💥 💥")
# print("===================================")





# import time
# import subprocess
# import msvcrt
# import random

# # 사용할 미끼 키 목록
# REAL_DEFUSE_KEY = 'x'  # 진짜 해제 키 (b'\x01',b'\x02', b'\x03')


# total_seconds = 100.0
# start_time = time.time()

# is_defused = False
# current_taunt = "시한폭탄이 작동 중입니다. 조심하세요!"
# incorrect_attempts = 0  # 틀린 시도 횟수

# while is_defused == False:
#     elapsed = time.time() - start_time
#     remaining = total_seconds - elapsed
    
#     if remaining <= 0:
#         is_defused = True
#         break
        
#     subprocess.run('cls', shell=True)
#     print("==================================================")
#     print("       ⚠️  보안 등급: 시한폭탄 활성화  ⚠️           ")
#     print("==================================================")
#     print(f"  💣 폭파까지 남은 시간: {remaining:.1f}초         ")
#     print(f"  🔑       해체 키를 누르세요!                     ")
#     print("==================================================")
#     print(f"  💬 [System]: {current_taunt}                  ")
#     print("==================================================")
    
#     # 키보드 입력 감지
#     if msvcrt.kbhit():
#         ch = msvcrt.getch().decode('utf-8').lower()
       
#         if ch == REAL_DEFUSE_KEY:
#             # [정답 처리] F1 등 특수 키를 누르면 폭탄 해제!
#             is_defused = True
#             break
#         else:
#             # 1. 미끼 키 변경
#             new_key = ch
            
#             # 2. 시간 차감 (1.5초)
#             start_time -= 1.5
            
#             # 3. 틀렸을 때 놀림말 출력
#             incorrect_attempts += 1
#             current_taunt = f"({incorrect_attempts}번 째 틀렸습니다!)"
            
#     time.sleep(0.1)

# # --- 최종 결과 출력 ---
# subprocess.run('cls', shell=True)
# print("==================================================")
# if is_defused:
#     print("🎉 [SUCCESS] 이~~이~~잉, 뭐여, 핸겨?!!!!")
# else:
#     print("💥 💥 💥 [BOOM] 펑! 멍청, 손가락 삐꾸, 주님, 거 쓸모없는 거 하나 올라가유!!!! 💥 💥 💥")
# print("==================================================")

