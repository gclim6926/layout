import json
from data_processor import DataProcessor
from visualize2 import create_visualizations
from config import OUTPUT_FILE, LAYOUT_FILE
from layout_validator import LayoutValidator

def main():
    """메인 실행 함수"""
    print("=== Layout Generator ===")
    
    # 1. 데이터 처리기 생성
    print("1. 데이터 처리기 초기화...")
    processor = DataProcessor()
    
    # 2. 전체 데이터 처리 과정 실행 (output.json 생성)
    print("2. 데이터 처리 및 output.json 생성...")
    processor.process_data(OUTPUT_FILE)
    
    # 3. output.json 검증 및 정리
    print("3. output.json 검증 및 정리...")
    validator = LayoutValidator()
    validator.validate_and_clean_layout_json(OUTPUT_FILE, LAYOUT_FILE)
    
    
    # 4. 시각화 생성
    print("4. 시각화 생성...")
    create_visualizations()
    
    print("=== 완료 ===")

if __name__ == '__main__':
    main() 