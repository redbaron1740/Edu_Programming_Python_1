import subprocess
import msvcrt
import time

# --- 메뉴 상수 선언 ---
DISP_SUB_MENU_DRINK                 = '1'
DISP_SUB_MENU_FOOD                  = '2'
DISP_SUB_MENU_MD                    = '3'
PROGRAM_QUIT                        = 'q'

# 음료 서브 메뉴 번호 규칙 (상수 정의)
DISP_SUB_MENU_DRINK_COFFEE          = 1
DISP_SUB_MENU_DRINK_TEA             = 2
DISP_SUB_MENU_DRINK_ADE_JUICE       = 3
DISP_SUB_MENU_DRINK_SMOOTHIE_FRAPPE = 4
DISP_SUB_MENU_DRINK_DECAFFE         = 5
DISP_SUB_MENU_DRINK_BEVERAGE        = 6
DISP_SUB_MENU_DRINK_BRAND_NEW       = 7
DISP_SUB_MENU_DRINK_BACK            = 8

# --- 데이터베이스 ---
Drink_Coffee_Menu = {
    '메가리카노 아이스': 3300,
    '아메리카노': 1700,
    '왕메가헛개리카노 아이스': 3400,
    '헛개리카노': 2400,
    '왕할메가커피 아이스': 3400,
    '할메가커피': 2300,
}

Drink_Tea_Menu = {
    '저당 골든애플 블랙티': 3500,
    '왕메가아이스티': 3900,
    '복숭아아이스티': 3000,
    '제로 복숭아 아이스티':3000,
    '제로 레몬말차 아이스티':2400
}

Drink_Ade_Juice_Menu = {
    '제로 부스트 에이드': 3000,
    '메가에이드': 3900,
    '레몬에이드': 3500,
    '자몽에이드':2400,
    '딸기주스':4000    
}

Drink_Smoothe_Frappe_Menu = {
    '자몽 톡톡 스무디': 4000,
    '저당 꿀배 XO야쿠르트': 3700,
    '밀크쉐이크': 2900,
    '플레인퐁크러쉬': 3900,
    '초코허니퐁크러쉬': 3900
}

Drink_All_list = [
    Drink_Coffee_Menu,
    Drink_Tea_Menu,
    Drink_Ade_Juice_Menu,
    Drink_Smoothe_Frappe_Menu
]

def display_clear():
    """화면 청소"""
    subprocess.run('cls', shell=True)

def display_main_menu():
    """메인 메뉴 화면"""
    print('어서오세요. MGC 키오스크입니다.')
    print('##### !!!  MGC 가을 시즌 신메뉴 출시 !!! ######')
    print('#########     All of MGC Menu      #########')
    print('# 1. 🥤 음료 ')
    print('# 2. 🍕 푸드 ')
    print('# 3. 🎁 상품 ')
    print('🛑 프로그램 종료는 q를 눌러주세요.')
    return input('선택해주세요(1-3, q): ').strip().lower()
    
def display_drink_sub_menu():
    """음료 서브 메뉴 화면"""
    print('#########     MGC Drink Menu      #########')
    print('# 1. 커피 ')
    print('# 2. 티 ')
    print('# 3. 에이드&주스 ')  
    print('# 4. 스무디&프라페 ')  
    print('# 5. 디카페인 ')  
    print('# 6. 음료 ')  
    print('# 7. 신상품 ')  
    print('# 8. ↩️  상위 메뉴 ')
    
    try:
        return int(input('선택해주세요(1-8): '))
    except ValueError:
        return -1  # 잘못된 문자 입력 시 예외 처리용 값 리턴

def display_drink_all_sub_menu(category = DISP_SUB_MENU_DRINK_COFFEE):
    """음료 전체 서브 메뉴 목록 화면"""
    sub_menu_cate_str = ""
    index = 1
    menu_list = []
    
    if category == DISP_SUB_MENU_DRINK_COFFEE:
        sub_menu_cate_str = "Coffee"
    elif category == DISP_SUB_MENU_DRINK_TEA:
        sub_menu_cate_str = "Tea"
    elif category == DISP_SUB_MENU_DRINK_ADE_JUICE:
        sub_menu_cate_str = "Ade & Juice"
    elif category == DISP_SUB_MENU_DRINK_SMOOTHIE_FRAPPE:
        sub_menu_cate_str = "Smoothie & Frappe"
    
    menu_dict = Drink_All_list[category - 1]
    
    print(f"#########     MGC {sub_menu_cate_str} Menu      #########")
    
    for item, price in menu_dict.items():
        print(f'# {index}. \t 품명: {item}\n# \t가격: {price}원')
        index += 1
    
    print(f'# {index}. ↩️  상위 메뉴 ')
    
    try:
        sel = int(input(f'선택해주세요(1-{index}): '))
    except ValueError:
        return {}
    
    # [버그 수정]: 올바른 상품 범위를 선택했는지 검증 (1번부터 메뉴 개수까지)
    if 1 <= sel <= len(menu_dict):
        sel_item, sel_price = list(menu_dict.items())[sel-1]
        return {sel_item: sel_price}
    else:
        return {}  # 상위 메뉴 번호를 누르거나 범위 초과 시 빈 딕셔너리 반환

def calculate_pay_process(selected_product):
    """결제 프로세스 로직"""
    if not selected_product:
        return

    print('# 선택하신 상품은 다음과 같습니다.')
    coffee, price = list(selected_product.items())[0]
    original_price = price  # 취소 시 안내를 위해 원가 저장
    
    print('＃＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝\n')
    print(f'# 상품명: {coffee}')    
    print(f'# 결제 금액: {original_price}원 \n\n')    
    
    proceed = input('결제하시겠습니까? (y/n): ').strip().lower()
    
    # [버그 수정]: 사용자가 'n'을 누르면 결제를 즉시 취소하고 탈출
    if proceed == 'y':
        
        while True:
            try:
                payed_cash = int(input('# 현금을 넣으세요: '))
            except ValueError:
                print('숫자로만 정확한 금액을 입력해주세요.')
                continue

            print(f'현금 {payed_cash}원을 받았습니다.')
                
            if payed_cash > price: 
                print(f'잔돈 {payed_cash - price}원 받으세요.\n')
                break
            elif payed_cash < price:
                price -= payed_cash
                # [버그 수정]: 줄바꿈 기호 오타 /n -> \n 변경
                print(f'결제 금액이 {price}원 모자랍니다. 금액을 더 넣어주세요.\n')    
            elif payed_cash == price:
                break
                    
        print('결제가 완료되었습니다. \n감사합니다. 또 오세요.')
        time.sleep(2)
    else:
        print('결제가 취소되었습니다. 메인 화면으로 돌아갑니다.')
        time.sleep(1.5)

def main():
    while True:
        last_sel_product = {}
        display_clear()
        sel_menu = display_main_menu()
        
        if sel_menu == DISP_SUB_MENU_DRINK:
            while True:  # 음료 서브메뉴 루프
                display_clear()
                sel_sub_menu = display_drink_sub_menu()

                if DISP_SUB_MENU_DRINK_COFFEE <= sel_sub_menu and \
                        sel_sub_menu <= DISP_SUB_MENU_DRINK_ADE_JUICE :
                      display_clear()
                      last_sel_product = display_drink_all_sub_menu(sel_sub_menu)
                      
                      if last_sel_product:
                          break

                elif sel_sub_menu == DISP_SUB_MENU_DRINK_BACK:
                    break  # 상위 메뉴로 돌아가기
                    
                elif sel_sub_menu == -1:
                    print('올바른 숫자를 입력해주세요.')
                    time.sleep(1)
                else:
                    print('준비 중이거나 없는 메뉴 번호입니다.')
                    time.sleep(1)
            
            # 상품이 선택된 경우 결제창 띄우기
            if last_sel_product:
                display_clear()
                calculate_pay_process(last_sel_product)
                 
        elif sel_menu == PROGRAM_QUIT:
            print('프로그램을 종료합니다. 이용해 주셔서 감사합니다.')
            break
        elif sel_menu in [DISP_SUB_MENU_FOOD, DISP_SUB_MENU_MD]:
            print('해당 카테고리는 현재 준비 중입니다.')
            time.sleep(1.5)
        else:
            print('잘못된 입력입니다. 1, 2, 3 또는 q를 입력하세요.')
            time.sleep(1.5)

if __name__ == '__main__':
    main()
