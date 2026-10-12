
import json

def load_json(file_path):
    """
    with 문을 사용하지 않고 open()과 close()로 JSON 파일을 읽어오는 함수
    """
    fp = None
    try:
        # 1. 파일 열기 (읽기 모드)
        fp = open(file_path, "r", encoding="utf-8")
        
        # 2. JSON 데이터 읽기
        data = json.load(fp)
        print(f"[{file_path}] 파일을 성공적으로 불러왔습니다.")
        return data
        
    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return None
    except json.JSONDecodeError:
        print("오류: JSON 파일의 형식이 잘못되었습니다.")
        return None
    finally:
        # 3. 파일 닫기
        if fp is not None:
            fp.close()

def main():
    file_path = "student.json"

    # 파일 저장 및 불러오기 실행
    loaded_data = load_json(file_path)

    if loaded_data:
        print("\n--- 읽어온 데이터 출력 ---")
        print(f"이름: {loaded_data['name']}")
        print(f"전공: {loaded_data['major']}")    


# --- [실행 및 테스트 예시] ---
if __name__ == "__main__":
    main()