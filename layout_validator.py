import json
from config import OUTPUT_FILE, LAYOUT_FILE

class LayoutValidator:
    def __init__(self):
        pass
    
    def validate_and_clean_layout_json(self, input_file=OUTPUT_FILE, output_file=LAYOUT_FILE):
        """output.json 검증 및 겹치는 데이터 정리 함수"""
        print("=== output.json 검증 및 정리 시작 ===")
        
        # output.json 읽기
        try:
            with open(input_file, 'r', encoding='utf-8') as f:
                layout_data = json.load(f)
        except FileNotFoundError:
            print(f"❌ {input_file} 파일을 찾을 수 없습니다.")
            return
        except json.JSONDecodeError:
            print(f"❌ {input_file} 파일의 JSON 형식이 올바르지 않습니다.")
            return
        
        addresses = layout_data.get('addresses', [])
        lines = layout_data.get('lines', [])
        
        print(f"📊 검증 대상: {len(addresses)}개 address, {len(lines)}개 line")
        
        # 1. Address 좌표 겹침 검사 및 정리
        print("\n1. Address 좌표 겹침 검사 및 정리...")
        address_overlaps = self.find_address_overlaps(addresses)
        
        if address_overlaps:
            print(f"⚠️  겹치는 address 좌표 발견: {len(address_overlaps)}개 그룹")
            for i, overlap_group in enumerate(address_overlaps, 1):
                print(f"\n   그룹 {i}:")
                for addr in overlap_group:
                    print(f"     - ID: {addr['id']}, Address: {addr['address']}, Name: {addr['name']}")
                    print(f"       좌표: ({addr['pos']['x']}, {addr['pos']['y']}, {addr['pos']['z']})")
            
            # 겹치는 address 정리
            cleaned_addresses = self.clean_address_overlaps(addresses, address_overlaps)
            print(f"\n✅ Address 정리 완료: {len(addresses)}개 → {len(cleaned_addresses)}개")
        else:
            print("✅ 겹치는 address 좌표가 없습니다.")
            cleaned_addresses = addresses
        
        # 2. Line 좌표 겹침 검사 및 정리
        print("\n2. Line 좌표 겹침 검사 및 정리...")
        line_overlaps = self.find_line_overlaps(lines)
        
        if line_overlaps:
            print(f"⚠️  겹치는 line 좌표 발견: {len(line_overlaps)}개 그룹")
            for i, overlap_group in enumerate(line_overlaps, 1):
                print(f"\n   그룹 {i}:")
                for line in overlap_group:
                    print(f"     - ID: {line['id']}, Name: {line['name']}")
                    print(f"       From: ({line['fromPos']['x']}, {line['fromPos']['y']}, {line['fromPos']['z']})")
                    print(f"       To: ({line['toPos']['x']}, {line['toPos']['y']}, {line['toPos']['z']})")
            
            # 겹치는 line 정리
            cleaned_lines = self.clean_line_overlaps(lines, line_overlaps)
            print(f"\n✅ Line 정리 완료: {len(lines)}개 → {len(cleaned_lines)}개")
        else:
            print("✅ 겹치는 line 좌표가 없습니다.")
            cleaned_lines = lines
        
        # 3. layout.json 업데이트
        print("\n3. Layout.json 업데이트...")
        layout_data['addresses'] = cleaned_addresses
        layout_data['lines'] = cleaned_lines
        
        # 백업 파일 생성
        backup_file = output_file.replace('.json', '_backup.json')
        try:
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(layout_data, f, indent=2, ensure_ascii=False)
            print(f"📁 백업 파일 생성: {backup_file}")
        except Exception as e:
            print(f"⚠️  백업 파일 생성 실패: {e}")
        
        # 업데이트된 layout.json 저장
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(layout_data, f, indent=2, ensure_ascii=False)
            print(f"✅ {output_file} 업데이트 완료")
        except Exception as e:
            print(f"❌ {output_file} 업데이트 실패: {e}")
            return
        
        print(f"\n=== output.json 검증 및 정리 완료 ===")
        print(f"📊 최종 결과:")
        print(f"   - Address: {len(cleaned_addresses)}개")
        print(f"   - Lines: {len(cleaned_lines)}개")
        
        return cleaned_addresses, cleaned_lines
    
    def validate_layout_json(self, layout_file=OUTPUT_FILE):
        """output.json 검증 함수 (기존 함수 유지)"""
        print("=== output.json 검증 시작 ===")
        
        # output.json 읽기
        try:
            with open(layout_file, 'r', encoding='utf-8') as f:
                layout_data = json.load(f)
        except FileNotFoundError:
            print(f"❌ {layout_file} 파일을 찾을 수 없습니다.")
            return
        except json.JSONDecodeError:
            print(f"❌ {layout_file} 파일의 JSON 형식이 올바르지 않습니다.")
            return
        
        addresses = layout_data.get('addresses', [])
        lines = layout_data.get('lines', [])
        
        print(f"📊 검증 대상: {len(addresses)}개 address, {len(lines)}개 line")
        
        # 1. Address 좌표 겹침 검사
        print("\n1. Address 좌표 겹침 검사...")
        address_overlaps = self.find_address_overlaps(addresses)
        
        if address_overlaps:
            print(f"⚠️  겹치는 address 좌표 발견: {len(address_overlaps)}개 그룹")
            for i, overlap_group in enumerate(address_overlaps, 1):
                print(f"\n   그룹 {i}:")
                for addr in overlap_group:
                    print(f"     - ID: {addr['id']}, Address: {addr['address']}, Name: {addr['name']}")
                    print(f"       좌표: ({addr['pos']['x']}, {addr['pos']['y']}, {addr['pos']['z']})")
        else:
            print("✅ 겹치는 address 좌표가 없습니다.")
        
        # 2. Line 좌표 겹침 검사
        print("\n2. Line 좌표 겹침 검사...")
        line_overlaps = self.find_line_overlaps(lines)
        
        if line_overlaps:
            print(f"⚠️  겹치는 line 좌표 발견: {len(line_overlaps)}개 그룹")
            for i, overlap_group in enumerate(line_overlaps, 1):
                print(f"\n   그룹 {i}:")
                for line in overlap_group:
                    print(f"     - ID: {line['id']}, Name: {line['name']}")
                    print(f"       From: ({line['fromPos']['x']}, {line['fromPos']['y']}, {line['fromPos']['z']})")
                    print(f"       To: ({line['toPos']['x']}, {line['toPos']['y']}, {line['toPos']['z']})")
        else:
            print("✅ 겹치는 line 좌표가 없습니다.")
        
        print("\n=== output.json 검증 완료 ===")

    def clean_address_overlaps(self, addresses, address_overlaps):
        """겹치는 address 정리 - 각 그룹에서 첫 번째만 유지"""
        addresses_to_remove = set()
        
        for overlap_group in address_overlaps:
            # 첫 번째 address는 유지하고 나머지는 제거 대상으로 표시
            for addr in overlap_group[1:]:
                addresses_to_remove.add(addr['id'])
        
        # 제거 대상이 아닌 address만 유지
        cleaned_addresses = [addr for addr in addresses if addr['id'] not in addresses_to_remove]
        
        return cleaned_addresses

    def clean_line_overlaps(self, lines, line_overlaps):
        """겹치는 line 정리 - 각 그룹에서 첫 번째만 유지"""
        lines_to_remove = set()
        
        for overlap_group in line_overlaps:
            # 첫 번째 line은 유지하고 나머지는 제거 대상으로 표시
            for line in overlap_group[1:]:
                lines_to_remove.add(line['id'])
        
        # 제거 대상이 아닌 line만 유지
        cleaned_lines = [line for line in lines if line['id'] not in lines_to_remove]
        
        return cleaned_lines

    def find_address_overlaps(self, addresses):
        """Address 좌표 겹침 찾기"""
        overlaps = []
        checked = set()
        
        for i, addr1 in enumerate(addresses):
            if i in checked:
                continue
                
            overlap_group = [addr1]
            pos1 = addr1['pos']
            
            for j, addr2 in enumerate(addresses[i+1:], i+1):
                if j in checked:
                    continue
                    
                pos2 = addr2['pos']
                
                # 좌표가 동일한지 확인 (소수점 오차 허용)
                if (abs(pos1['x'] - pos2['x']) < 1e-6 and 
                    abs(pos1['y'] - pos2['y']) < 1e-6 and 
                    abs(pos1['z'] - pos2['z']) < 1e-6):
                    overlap_group.append(addr2)
                    checked.add(j)
            
            if len(overlap_group) > 1:
                overlaps.append(overlap_group)
                checked.add(i)
        
        return overlaps

    def find_line_overlaps(self, lines):
        """Line 좌표 겹침 찾기 (fromPos/toPos 구분 없이)"""
        overlaps = []
        checked = set()
        
        for i, line1 in enumerate(lines):
            if i in checked:
                continue
                
            overlap_group = [line1]
            pos1_from = line1['fromPos']
            pos1_to = line1['toPos']
            
            for j, line2 in enumerate(lines[i+1:], i+1):
                if j in checked:
                    continue
                    
                pos2_from = line2['fromPos']
                pos2_to = line2['toPos']
                
                # 두 line의 좌표가 동일한지 확인 (순서 무관)
                if self.coordinates_match(pos1_from, pos1_to, pos2_from, pos2_to):
                    overlap_group.append(line2)
                    checked.add(j)
            
            if len(overlap_group) > 1:
                overlaps.append(overlap_group)
                checked.add(i)
        
        return overlaps

    def coordinates_match(self, pos1_from, pos1_to, pos2_from, pos2_to):
        """두 line의 좌표가 동일한지 확인 (순서 무관)"""
        # 첫 번째 방법: from1=from2, to1=to2
        match1 = (abs(pos1_from['x'] - pos2_from['x']) < 1e-6 and 
                  abs(pos1_from['y'] - pos2_from['y']) < 1e-6 and 
                  abs(pos1_from['z'] - pos2_from['z']) < 1e-6 and
                  abs(pos1_to['x'] - pos2_to['x']) < 1e-6 and 
                  abs(pos1_to['y'] - pos2_to['y']) < 1e-6 and 
                  abs(pos1_to['z'] - pos2_to['z']) < 1e-6)
        
        # 두 번째 방법: from1=to2, to1=from2
        match2 = (abs(pos1_from['x'] - pos2_to['x']) < 1e-6 and 
                  abs(pos1_from['y'] - pos2_to['y']) < 1e-6 and 
                  abs(pos1_from['z'] - pos2_to['z']) < 1e-6 and
                  abs(pos1_to['x'] - pos2_from['x']) < 1e-6 and 
                  abs(pos1_to['y'] - pos2_from['y']) < 1e-6 and 
                  abs(pos1_to['z'] - pos2_from['z']) < 1e-6)
        
        return match1 or match2


def main():
    """독립 실행용 메인 함수"""
    validator = LayoutValidator()
    
    # 검증만 실행
    # validator.validate_layout_json()
    
    # 검증 및 정리 실행
    validator.validate_and_clean_layout_json()


if __name__ == '__main__':
    main() 