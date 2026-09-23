#총 5과목 점수를 평균을 구하는 프로그램을 작성하시오. 리스트를 사용
import subprocess

subprocess.run('cls', shell=True)

과목_리스트 = ["국어", "영어", "수학", "과학", "사회"]
점수_리스트 = []

for 과목 in 과목_리스트:
    while True:
        try:
            점수 = float(input(f"{과목} 점수를 입력하세요: "))
            if 0 <= 점수 <= 100:
                점수_리스트.append(점수)
                break
            else:
                print("0에서 100 사이의 점수를 입력해주세요.")
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

평균 = sum(점수_리스트) / len(점수_리스트)
print(f"평균 점수: {평균:.2f}")


# import msvcrt
# import random

# # ==========================================
# # [학생 실습 영역] 학생들이 직접 놀릴 말을 리스트에 추가해보세요!
# # ==========================================
# taunt_messages = [
#     "푸하하! 거기가 아닌데요?",
#     "눈이 삐셨나요? 화면 안 보여요?",
#     "그렇게 눌러서 언제 해제하시게요~?",
#     "컴퓨터: '에이, 틀렸습니다. 다시 하세요!'",
#     "폭탄이 비웃고 있습니다: ㅋㅋ",
#     "손가락이 꼬이시나 봐요? 힘내세요!",
#     "시간은 흘러간다~ 째깍째깍 ⏰"
# ]
# # ==========================================

# # 사용할 미끼 키 목록
# FAKE_KEYS = ['q', 'w', 'e', 'r', 'a', 's', 'd', 'f']
# REAL_DEFUSE_KEY = [b'\x00', b'\xe0']  # 진짜 해제 키 (b'\x01',b'\x02', b'\x03')

# total_seconds = 100.0
# start_time = time.time()
# current_fake_key = random.choice(FAKE_KEYS)

# is_defused = False
# current_taunt = "시한폭탄이 작동 중입니다. 조심하세요!"

# while True:
#     elapsed = time.time() - start_time
#     remaining = total_seconds - elapsed
    
#     if remaining <= 0:
#         break
        
#     subprocess.run('cls', shell=True)
#     print("==================================================")
#     print("       ⚠️  보안 등급 극상: 시한폭탄 활성화  ⚠️")
#     print("==================================================")
#     print(f"  💣 폭파까지 남은 시간: {remaining:.1f}초")
#     print(f"  🔑 [화면 표시 해제키]: [{current_fake_key.upper()}] 키를 누르세요!")
#     print("==================================================")
#     print(f"  💬 [System]: {current_taunt}")
#     print("==================================================")
    
#     # 키보드 입력 감지
#     if msvcrt.kbhit():
#         ch = msvcrt.getch()
        
#         # F1~F12, 방향키 등 특수 키 신호 감지 (b'\x00' 또는 b'\xe0')
#         if ch in REAL_DEFUSE_KEY:
#             # 뒤따라오는 스캔 코드(두 번째 바이트)를 읽어서 버퍼에서 제거
#             msvcrt.getch()
            
#             # [정답 처리] F1 등 특수 키를 누르면 폭탄 해제!
#             is_defused = True
#             break
#         else:
#             # 1. 미끼 키 변경
#             new_key = random.choice(FAKE_KEYS)
#             current_fake_key = new_key
            
#             # 2. 시간 차감 (1.5초)
#             start_time -= 1.5
            
#             # 3. 틀렸을 때 놀림말 출력
#             current_taunt = random.choice(taunt_messages)
            
#     time.sleep(0.01)

# # --- 최종 결과 출력 ---
# subprocess.run('cls', shell=True)
# print("==================================================")
# if is_defused:
#     print("🎉 [SUCCESS] 이~~이~~잉, 뭐여, 핸겨?!!!!")
# else:
#     print("💥 💥 💥 [BOOM] 펑! 멍청, 손가락 삐꾸, 주님, 거 쓸모없는 거 하나 올라가유!!!! 💥 💥 💥")
# print("==================================================")



# import random
# import subprocess

# subprocess.run('cls', shell=True)

# # ==========================================
# # 1. 중복 허용 정답 생성 (0~9 사이 숫자 3개)
# # ==========================================
# #secret_numbers = [random.randint(0, 9) for _ in range(3)]
# secret_numbers = [0,0,0]  # 테스트용 정답 (중복 허용)

# for i in range(3):
#     secret_numbers[i] = random.randint(0, 9)
 
# print("=========================================")
# print("  ⚾ [중복 허용] 숫자야구 게임을 시작합니다! ⚾")
# print("=========================================")
# print("0부터 9까지 숫자 3개를 맞춰보세요.")
# print("💡 참고: 정답에 동일한 숫자가 들어갈 수 있습니다! (예: 112, 707)\n")

# try_count = 0

# # ==========================================
# # 2. 게임 메인 루프
# # ==========================================
# while True:
#     try_count += 1
    
#     # [입력 받기]
#     user_input = input(f"[{try_count}회차] 숫자 3개를 입력하세요 (예: 112): ").strip()
    
#     # [예외 처리] 3자리 숫자가 아니거나 문자가 섞인 경우
#     if len(user_input) != 3 or not user_input.isdigit():
#         print("⚠️ 0~9 사이의 숫자로 정확히 3자리를 입력해 주세요!\n")
#         continue
    
#     # 입력받은 문자열을 숫자 리스트로 변환
#     user_numbers = [0,0,0]  # 테스트용 입력 (중복 허용)
#     for i in range(3):
#         user_numbers[i] = int(user_input[i])
    
#     # ==========================================
#     # 3. Strike / Ball 판정 로직 (2단계 매칭)
#     # ==========================================
#     strikes = 0
#     balls = 0
    
#     # 매칭 여부를 플래그(True/False)로 관리
#     secret_matched = [False] * 3
#     user_matched = [False] * 3
    
#     # Step 1: Strike 판정 (위치와 숫자가 모두 일치)
#     for i in range(3):
#         if user_numbers[i] == secret_numbers[i]:
#             strikes += 1
#             secret_matched[i] = True
#             user_matched[i] = True
            
#     # Step 2: Ball 판정 (Strike로 매칭되지 않은 나머지 숫자 대상)
#     for i in range(3):
#         if not user_matched[i]:
#             for j in range(3):
#                 if not secret_matched[j] and user_numbers[i] == secret_numbers[j]:
#                     balls += 1
#                     secret_matched[j] = True  # 중복 매칭 방지
#                     break
                    
#     # ==========================================
#     # 4. 결과 출력
#     # ==========================================
#     print(f"👉 결과: {strikes} Strike, {balls} Ball")
    
#     # 3 Strike면 정답 처리 및 게임 종료
#     if strikes == 3:
#         print("\n🎉 [SUCCESS] 축하합니다! 정답을 맞추셨습니다!")
#         print(f"정답: {secret_numbers}")
#         print(f"총 시도 횟수: {try_count}회")
#         print("=========================================")
#         break
#     else:
#         if strikes == 0 and balls == 0:
#             print("OUT! 일치하는 숫자가 하나도 없습니다.")
#         print("-" * 40)