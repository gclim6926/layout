import pandas as pd
import numpy as np
import json
import math
from config import RANDOM_INTERVAL, OUTPUT_FILE, ADDRESS_ID_START, LINE_ID_START, INPUT_FILE, Y_LINE_PAIR_CONFIG

class DataProcessor:
    def __init__(self):
        self.input_file = INPUT_FILE
        self.intervals = RANDOM_INTERVAL
        self.address_id = ADDRESS_ID_START  # 전역 address ID 관리
        self.line_id = LINE_ID_START  # 전역 line ID 관리

    def read_input_json(self):
        """input.json에서 모든 데이터를 읽어서 DataFrame으로 변환"""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # x_axis_lines, y_axis_lines 읽기
        x_lines = data.get('x_axis_lines', [])
        y_lines = data.get('y_axis_lines', [])
        
        x_df = pd.DataFrame([
            {
                'fromPos': {'x': line[0][0], 'y': line[0][1], 'z': line[0][2]},
                'toPos': {'x': line[1][0], 'y': line[1][1], 'z': line[1][2]}
            } for line in x_lines
        ])
        y_df = pd.DataFrame([
            {
                'fromPos': {'x': line[0][0], 'y': line[0][1], 'z': line[0][2]},
                'toPos': {'x': line[1][0], 'y': line[1][1], 'z': line[1][2]}
            } for line in y_lines
        ])
        
        # 모든 shape 데이터 읽기
        shape1 = data.get('shape1', [])
        shape1_pos = data.get('shape1_pos', [])
        shape2 = data.get('shape2', [])
        shape2_pos = data.get('shape2_pos', [])
        shape3 = data.get('shape3', [])
        shape3_pos = data.get('shape3_pos', [])
        shape4 = data.get('shape4', [])
        shape4_pos = data.get('shape4_pos', [])
        shape5 = data.get('shape5', [])
        shape5_pos = data.get('shape5_pos', [])
        shape6 = data.get('shape6', [])
        shape6_pos = data.get('shape6_pos', [])
        shape7 = data.get('shape7', [])
        shape8 = data.get('shape8', [])
        
        # shape1을 DataFrame으로 변환
        shape1_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape1)
        ])
        
        # shape1_pos를 DataFrame으로 변환
        shape1_pos_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1],
                'z': coord[2], 
                'coord_index': i
            } for i, coord in enumerate(shape1_pos)
        ])
        
        # shape2를 DataFrame으로 변환
        shape2_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape2)
        ])
        
        # shape2_pos를 DataFrame으로 변환
        shape2_pos_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1],
                'z': coord[2], 
                'coord_index': i
            } for i, coord in enumerate(shape2_pos)
        ])
        
        # shape3을 DataFrame으로 변환
        shape3_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape3)
        ])
        
        # shape3_pos를 DataFrame으로 변환
        shape3_pos_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1],
                'z': coord[2], 
                'coord_index': i
            } for i, coord in enumerate(shape3_pos)
        ])
        
        # shape4를 DataFrame으로 변환
        shape4_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape4)
        ])
        
        # shape4_pos를 DataFrame으로 변환
        shape4_pos_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1],
                'z': coord[2], 
                'coord_index': i
            } for i, coord in enumerate(shape4_pos)
        ])
        
        # shape5를 DataFrame으로 변환
        shape5_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape5)
        ])
        
        # shape5_pos를 DataFrame으로 변환
        shape5_pos_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1],
                'z': coord[2], 
                'coord_index': i
            } for i, coord in enumerate(shape5_pos)
        ])
        
        # shape6을 DataFrame으로 변환
        shape6_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape6)
        ])
        
        # shape6_pos를 DataFrame으로 변환
        shape6_pos_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1],
                'z': coord[2], 
                'coord_index': i
            } for i, coord in enumerate(shape6_pos)
        ])
        
        # shape7을 DataFrame으로 변환 (area)
        shape7_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape7)
        ])
        
        # shape8을 DataFrame으로 변환 (area)
        shape8_df = pd.DataFrame([
            {
                'x': coord[0],
                'y': coord[1], 
                'z': coord[2],
                'coord_index': i
            } for i, coord in enumerate(shape8)
        ])
        
        print(f"📊 Input JSON 데이터 읽기 완료")
        # print(f"   - x_axis_lines: {len(x_lines)}개")
        # print(f"   - y_axis_lines: {len(y_lines)}개")
        # print(f"   - shape1: {len(shape1)}개 좌표")
        # print(f"   - shape1_pos: {len(shape1_pos)}개 좌표")
        # print(f"   - shape2: {len(shape2)}개 좌표")
        # print(f"   - shape2_pos: {len(shape2_pos)}개 좌표")
        # print(f"   - shape3: {len(shape3)}개 좌표")
        # print(f"   - shape3_pos: {len(shape3_pos)}개 좌표")
        # print(f"   - shape4: {len(shape4)}개 좌표")
        # print(f"   - shape4_pos: {len(shape4_pos)}개 좌표")
        # print(f"   - shape5: {len(shape5)}개 좌표")
        # print(f"   - shape5_pos: {len(shape5_pos)}개 좌표")
        # print(f"   - shape6: {len(shape6)}개 좌표")
        # print(f"   - shape6_pos: {len(shape6_pos)}개 좌표")
        # print(f"   - shape7: {len(shape7)}개 좌표 (area)")
        # print(f"   - shape8: {len(shape8)}개 좌표 (area)")
        
        return x_df, y_df, shape1_df, shape1_pos_df, shape2_df, shape2_pos_df, shape3_df, shape3_pos_df, shape4_df, shape4_pos_df, shape5_df, shape5_pos_df, shape6_df, shape6_pos_df, shape7_df, shape8_df

    def make_addresses(self, lines, shape1_df=None, shape1_pos_df=None, shape2_df=None, shape2_pos_df=None, 
                      shape3_df=None, shape3_pos_df=None, shape4_df=None, shape4_pos_df=None,
                      shape5_df=None, shape5_pos_df=None, shape6_df=None, shape6_pos_df=None):
        """라인을 따라 address들을 생성하고 모든 shape address도 추가"""
        addresses = []
        
        # x/y_axis_lines address 생성
        for _, line in lines.iterrows():
            x1 = line['fromPos']['x']
            y1 = line['fromPos']['y']
            z1 = line['fromPos']['z']
            x2 = line['toPos']['x']
            y2 = line['toPos']['y']
            z2 = line['toPos']['z']
            line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            # 시작점 추가
            addresses.append({
                'id': self.address_id,
                'address': self.address_id,
                'name': f'ADDR_{self.address_id}',
                'pos': {'x': x1, 'y': y1, 'z': z1}
            })
            self.address_id += 1
            # 중간점들 추가
            current_distance = 0
            while current_distance < line_length:
                interval = np.random.choice(self.intervals)
                current_distance += interval
                if current_distance >= line_length:
                    break
                t = current_distance / line_length
                x = x1 + t * (x2 - x1)
                y = y1 + t * (y2 - y1)
                z = z1 + t * (z2 - z1)
                addresses.append({
                    'id': self.address_id,
                    'address': self.address_id,
                    'name': f'ADDR_{self.address_id}',
                    'pos': {'x': x, 'y': y, 'z': z}
                })
                self.address_id += 1
            # 끝점 추가
            addresses.append({
                'id': self.address_id,
                'address': self.address_id,
                'name': f'ADDR_{self.address_id}',
                'pos': {'x': x2, 'y': y2, 'z': z2}
            })
            self.address_id += 1
        
        # 모든 shape address 생성
        shape_dfs = [
            (shape1_df, shape1_pos_df, "shape1"),
            (shape2_df, shape2_pos_df, "shape2"),
            (shape3_df, shape3_pos_df, "shape3"),
            (shape4_df, shape4_pos_df, "shape4"),
            (shape5_df, shape5_pos_df, "shape5"),
            (shape6_df, shape6_pos_df, "shape6")
        ]
        
        for shape_df, shape_pos_df, shape_name in shape_dfs:
            if shape_df is not None and shape_pos_df is not None:
                # shape_df에 있는 모든 좌표는 addresses에 새롭게 추가
                for _, row in shape_df.iterrows():
                    addresses.append({
                        'id': self.address_id,
                        'address': self.address_id,
                        'name': f'ADDR_{self.address_id}',
                        'pos': {'x': row['x'], 'y': row['y'], 'z': row['z']}
                    })
                    self.address_id += 1
                
                # shape_pos_df에 있는 모든 점에 대해 shape와 동일한 모양의 addresses 생성
                if len(shape_pos_df) > 0 and len(shape_df) > 0:
                    # shape의 첫 번째 좌표를 원본 기준점으로 사용
                    original_base = shape_df.iloc[0]
                    original_x, original_y, original_z = original_base['x'], original_base['y'], original_base['z']
                    
                    # shape_pos_df의 각 점에 대해 반복
                    for pos_idx, pos_row in shape_pos_df.iterrows():
                        # 현재 shape_pos 점을 새로운 기준점으로 사용
                        base_x, base_y, base_z = pos_row['x'], pos_row['y'], pos_row['z']
                        
                        # offset 계산 (현재 기준점 - 원본 기준점)
                        x_offset = base_x - original_x
                        y_offset = base_y - original_y
                        z_offset = base_z - original_z
                        
                        # shape의 모든 좌표에 offset을 적용하여 새로운 address 생성
                        for _, shape_row in shape_df.iterrows():
                            x, y, z = shape_row['x'], shape_row['y'], shape_row['z']
                            new_x = x + x_offset
                            new_y = y + y_offset
                            new_z = z + z_offset
                            
                            addresses.append({
                                'id': self.address_id,
                                'address': self.address_id,
                                'name': f'ADDR_{self.address_id}',
                                'pos': {'x': new_x, 'y': new_y, 'z': new_z}
                            })
                            self.address_id += 1
        

        
        return pd.DataFrame(addresses)

    def generate_area_lines(self, area_df, z_value):
        """area 영역 내에서 사각형 외각 이중라인과 내부 임의 라인들을 생성"""
        if len(area_df) < 2:
            return pd.DataFrame()
        
        # area의 경계 계산
        min_x = area_df['x'].min()
        max_x = area_df['x'].max()
        min_y = area_df['y'].min()
        max_y = area_df['y'].max()
        
        area_lines = []
        gap = 33.33  # 이중라인 간격
        min_line_distance = 21.667  # 라인 간 최소 거리
        
        # 1. 사각형 외각 이중라인 생성 (gap 33.33)
        # 바깥쪽 사각형
        outer_lines = [
            # 하단 가로선
            {'fromPos': {'x': min_x, 'y': min_y, 'z': z_value}, 'toPos': {'x': max_x, 'y': min_y, 'z': z_value}},
            # 우측 세로선
            {'fromPos': {'x': max_x, 'y': min_y, 'z': z_value}, 'toPos': {'x': max_x, 'y': max_y, 'z': z_value}},
            # 상단 가로선
            {'fromPos': {'x': max_x, 'y': max_y, 'z': z_value}, 'toPos': {'x': min_x, 'y': max_y, 'z': z_value}},
            # 좌측 세로선
            {'fromPos': {'x': min_x, 'y': max_y, 'z': z_value}, 'toPos': {'x': min_x, 'y': min_y, 'z': z_value}}
        ]
        
        # 안쪽 사각형
        inner_lines = [
            # 하단 가로선
            {'fromPos': {'x': min_x + gap, 'y': min_y + gap, 'z': z_value}, 'toPos': {'x': max_x - gap, 'y': min_y + gap, 'z': z_value}},
            # 우측 세로선
            {'fromPos': {'x': max_x - gap, 'y': min_y + gap, 'z': z_value}, 'toPos': {'x': max_x - gap, 'y': max_y - gap, 'z': z_value}},
            # 상단 가로선
            {'fromPos': {'x': max_x - gap, 'y': max_y - gap, 'z': z_value}, 'toPos': {'x': min_x + gap, 'y': max_y - gap, 'z': z_value}},
            # 좌측 세로선
            {'fromPos': {'x': min_x + gap, 'y': max_y - gap, 'z': z_value}, 'toPos': {'x': min_x + gap, 'y': min_y + gap, 'z': z_value}}
        ]
        
        area_lines.extend(outer_lines)
        area_lines.extend(inner_lines)
        
        # 2. 안쪽 x축 라인 생성 (길게만)
        # 길게 (90-99% 길이)
        num_x_long = np.random.randint(5, 7)  # 5-7개의 긴 x축 라인
        x_positions = []  # 생성된 x 위치들을 저장
        
        for i in range(num_x_long):
            attempts = 0
            max_attempts = 100  # 최대 시도 횟수
            
            while attempts < max_attempts:
                x_pos = min_x + gap + (max_x - min_x - 2*gap) * np.random.random()
                
                # 기존 x축 라인들과의 거리 체크
                too_close = False
                for existing_x in x_positions:
                    if abs(x_pos - existing_x) < min_line_distance:
                        too_close = True
                        break
                
                if not too_close:
                    x_positions.append(x_pos)
                    # 긴 길이 (90~99%)
                    line_length = np.random.uniform(0.9, 0.99) * (max_y - min_y - 2*gap)
                    y_start = min_y + gap + (max_y - min_y - 2*gap - line_length) * np.random.random()
                    y_end = y_start + line_length
                    
                    area_lines.append({
                        'fromPos': {'x': x_pos, 'y': y_start, 'z': z_value},
                        'toPos': {'x': x_pos, 'y': y_end, 'z': z_value}
                    })
                    break
                
                attempts += 1
        
        # 3. 안쪽 y축 라인 생성 (길게만)
        # 길게 (90-99% 길이)
        num_y_long = np.random.randint(10, 12)  # 10-12개의 긴 y축 라인
        y_positions = []  # 생성된 y 위치들을 저장
        
        for i in range(num_y_long):
            attempts = 0
            max_attempts = 100  # 최대 시도 횟수
            
            while attempts < max_attempts:
                y_pos = min_y + gap + (max_y - min_y - 2*gap) * np.random.random()
                
                # 기존 y축 라인들과의 거리 체크
                too_close = False
                for existing_y in y_positions:
                    if abs(y_pos - existing_y) < min_line_distance:
                        too_close = True
                        break
                
                if not too_close:
                    y_positions.append(y_pos)
                    # 긴 길이 (90-99%)
                    line_length = np.random.uniform(0.9, 0.99) * (max_x - min_x - 2*gap)
                    x_start = min_x + gap + (max_x - min_x - 2*gap - line_length) * np.random.random()
                    x_end = x_start + line_length
                    
                    area_lines.append({
                        'fromPos': {'x': x_start, 'y': y_pos, 'z': z_value},
                        'toPos': {'x': x_end, 'y': y_pos, 'z': z_value}
                    })
                    break
                
                attempts += 1
        
        return pd.DataFrame(area_lines)

    def find_y_line_pairs(self, y_axis_lines):
        """y_axis_lines에서 조건에 맞는 pair들을 찾음"""
        pairs = []
        
        # y line들의 정보 계산
        y_lines_info = []
        for i, line in y_axis_lines.iterrows():
            from_pos = line['fromPos']
            to_pos = line['toPos']
            
            # 길이 계산
            length = abs(to_pos['y'] - from_pos['y'])
            
            # 중간값 계산
            mid_y = (from_pos['y'] + to_pos['y']) / 2
            
            y_lines_info.append({
                'index': i,
                'line': line,
                'length': length,
                'mid_y': mid_y,
                'x_pos': from_pos['x'],  # y line의 x 위치
                'y_start': min(from_pos['y'], to_pos['y']),
                'y_end': max(from_pos['y'], to_pos['y'])
            })
        
        # 첫 번째 범위 (3600~3800) 조건에 맞는 y line들 필터링
        valid_lines_1 = [
            info for info in y_lines_info 
            if (info['length'] >= Y_LINE_PAIR_CONFIG['min_length'] and
                Y_LINE_PAIR_CONFIG['mid_range_min'] <= info['mid_y'] <= Y_LINE_PAIR_CONFIG['mid_range_max'])
        ]
        
        # 두 번째 범위 (5300~5500) 조건에 맞는 y line들 필터링
        valid_lines_2 = [
            info for info in y_lines_info 
            if (info['length'] >= Y_LINE_PAIR_CONFIG['min_length'] and
                Y_LINE_PAIR_CONFIG['mid_range_min_2'] <= info['mid_y'] <= Y_LINE_PAIR_CONFIG['mid_range_max_2'])
        ]
        
        # 첫 번째 범위 pair 찾기 (60~100 떨어진 y line들)
        for i, line1_info in enumerate(valid_lines_1):
            for j, line2_info in enumerate(valid_lines_1[i+1:], i+1):
                # 두 y line 간의 거리 계산
                distance = abs(line1_info['x_pos'] - line2_info['x_pos'])
                
                # pair 간격 조건 확인
                if (Y_LINE_PAIR_CONFIG['pair_distance_min'] <= distance <= 
                    Y_LINE_PAIR_CONFIG['pair_distance_max']):
                    pairs.append((line1_info, line2_info, 'range1'))
        
        # 두 번째 범위 pair 찾기 (60~100 떨어진 y line들)
        for i, line1_info in enumerate(valid_lines_2):
            for j, line2_info in enumerate(valid_lines_2[i+1:], i+1):
                # 두 y line 간의 거리 계산
                distance = abs(line1_info['x_pos'] - line2_info['x_pos'])
                
                # pair 간격 조건 확인
                if (Y_LINE_PAIR_CONFIG['pair_distance_min'] <= distance <= 
                    Y_LINE_PAIR_CONFIG['pair_distance_max']):
                    pairs.append((line1_info, line2_info, 'range2'))
        
        return pairs

    def create_pair_lines(self, pairs, addresses):
        """pair에 대한 line들을 생성"""
        pair_lines = []
        
        for line1_info, line2_info, pair_range in pairs:
            # 각 y line에서 address 찾기
            line1_addresses = self.find_addresses_on_line(addresses, line1_info['x_pos'], line1_info['line']['fromPos']['z'])
            line2_addresses = self.find_addresses_on_line(addresses, line2_info['x_pos'], line2_info['line']['fromPos']['z'])
            
            if pair_range == 'range1':
                # 첫 번째 범위 (3600~3800): 3600 근처 -> 3800 근처
                # 3600 근처 address 찾기
                near_3600_line1 = self.find_address_near_y(line1_addresses, Y_LINE_PAIR_CONFIG['y_near_3600'])
                near_3600_line2 = self.find_address_near_y(line2_addresses, Y_LINE_PAIR_CONFIG['y_near_3600'])
                
                # 3800 근처 address 찾기
                near_3800_line1 = self.find_address_near_y(line1_addresses, Y_LINE_PAIR_CONFIG['y_near_3800'])
                near_3800_line2 = self.find_address_near_y(line2_addresses, Y_LINE_PAIR_CONFIG['y_near_3800'])
                
                # 첫 번째 line 생성: line1의 3600 근처 -> line2의 3800 근처
                if near_3600_line1 and near_3800_line2:
                    pair_lines.append({
                        'id': self.line_id,
                        'name': f'PAIR_LINE_{near_3600_line1["id"]}_{near_3800_line2["id"]}',
                        'fromAddress': near_3600_line1['id'],
                        'toAddress': near_3800_line2['id'],
                        'fromPos': near_3600_line1['pos'],
                        'toPos': near_3800_line2['pos'],
                        'curve': False
                    })
                    self.line_id += 1
                
                # 두 번째 line 생성: line2의 3600 근처 -> line1의 3800 근처
                if near_3600_line2 and near_3800_line1:
                    pair_lines.append({
                        'id': self.line_id,
                        'name': f'PAIR_LINE_{near_3600_line2["id"]}_{near_3800_line1["id"]}',
                        'fromAddress': near_3600_line2['id'],
                        'toAddress': near_3800_line1['id'],
                        'fromPos': near_3600_line2['pos'],
                        'toPos': near_3800_line1['pos'],
                        'curve': False
                    })
                    self.line_id += 1
            
            elif pair_range == 'range2':
                # 두 번째 범위 (5300~5500): 5300 근처 -> 5500 근처
                # 5300 근처 address 찾기
                near_5300_line1 = self.find_address_near_y(line1_addresses, Y_LINE_PAIR_CONFIG['y_near_5300'])
                near_5300_line2 = self.find_address_near_y(line2_addresses, Y_LINE_PAIR_CONFIG['y_near_5300'])
                
                # 5500 근처 address 찾기
                near_5500_line1 = self.find_address_near_y(line1_addresses, Y_LINE_PAIR_CONFIG['y_near_5500'])
                near_5500_line2 = self.find_address_near_y(line2_addresses, Y_LINE_PAIR_CONFIG['y_near_5500'])
                
                # 첫 번째 line 생성: line1의 5300 근처 -> line2의 5500 근처
                if near_5300_line1 and near_5500_line2:
                    pair_lines.append({
                        'id': self.line_id,
                        'name': f'PAIR_LINE_{near_5300_line1["id"]}_{near_5500_line2["id"]}',
                        'fromAddress': near_5300_line1['id'],
                        'toAddress': near_5500_line2['id'],
                        'fromPos': near_5300_line1['pos'],
                        'toPos': near_5500_line2['pos'],
                        'curve': False
                    })
                    self.line_id += 1
                
                # 두 번째 line 생성: line2의 5300 근처 -> line1의 5500 근처
                if near_5300_line2 and near_5500_line1:
                    pair_lines.append({
                        'id': self.line_id,
                        'name': f'PAIR_LINE_{near_5300_line2["id"]}_{near_5500_line1["id"]}',
                        'fromAddress': near_5300_line2['id'],
                        'toAddress': near_5500_line1['id'],
                        'fromPos': near_5300_line2['pos'],
                        'toPos': near_5500_line1['pos'],
                        'curve': False
                    })
                    self.line_id += 1
        
        return pair_lines

    def find_addresses_on_line(self, addresses, x_pos, z_value):
        """특정 y line 위의 모든 address 찾기"""
        line_addresses = []
        
        for _, addr in addresses.iterrows():
            if (abs(addr['pos']['x'] - x_pos) < 1e-6 and 
                abs(addr['pos']['z'] - z_value) < 1e-6):
                line_addresses.append(addr.to_dict())
        
        return line_addresses

    def find_address_near_y(self, addresses, target_y):
        """특정 y 값 근처의 가장 가까운 address 찾기"""
        nearest_address = None
        min_distance = float('inf')
        tolerance = Y_LINE_PAIR_CONFIG['near_tolerance']
        
        for addr in addresses:
            distance = abs(addr['pos']['y'] - target_y)
            if distance <= tolerance and distance < min_distance:
                min_distance = distance
                nearest_address = addr
        
        return nearest_address

    def make_lines_from_addresses(self, addresses, input_lines, shape1_df=None, shape1_pos_df=None, 
                                 shape2_df=None, shape2_pos_df=None, shape3_df=None, shape3_pos_df=None, 
                                 shape4_df=None, shape4_pos_df=None, shape5_df=None, shape5_pos_df=None,
                                 shape6_df=None, shape6_pos_df=None):
        """address들을 연결하는 lines 생성하고 모든 shape lines도 추가"""
        lines = []
        
        # 기존 라인 address 연결
        for line_idx, input_line in input_lines.iterrows():
            x1 = input_line['fromPos']['x']
            y1 = input_line['fromPos']['y']
            x2 = input_line['toPos']['x']
            y2 = input_line['toPos']['y']
            # 해당 라인 위에 있는 address들 찾기
            line_addresses = addresses[
                addresses['pos'].apply(
                    lambda pos: (
                        min(x1, x2) <= pos['x'] <= max(x1, x2) and
                        min(y1, y2) <= pos['y'] <= max(y1, y2) and
                        abs((y2 - y1) * (pos['x'] - x1) - (x2 - x1) * (pos['y'] - y1)) < 1e-6
                    )
                )
            ].sort_values(by=['pos'], key=lambda x: x.apply(lambda pos: (pos['x'] - x1) ** 2 + (pos['y'] - y1) ** 2))
            # 연속된 address들을 연결하는 lines 생성
            for i in range(len(line_addresses) - 1):
                from_addr = line_addresses.iloc[i]
                to_addr = line_addresses.iloc[i + 1]
                lines.append({
                    'id': self.line_id,
                    'name': f'LINE_{from_addr["id"]}_{to_addr["id"]}',
                    'fromAddress': from_addr['id'],
                    'toAddress': to_addr['id'],
                    'fromPos': from_addr['pos'],
                    'toPos': to_addr['pos'],
                    'curve': False
                })
                self.line_id += 1
        
        # 모든 shape lines 생성
        shape_dfs = [
            (shape1_df, shape1_pos_df, "shape1"),
            (shape2_df, shape2_pos_df, "shape2"),
            (shape3_df, shape3_pos_df, "shape3"),
            (shape4_df, shape4_pos_df, "shape4"),
            (shape5_df, shape5_pos_df, "shape5"),
            (shape6_df, shape6_pos_df, "shape6")
        ]
        
        for shape_df, shape_pos_df, shape_name in shape_dfs:
            if shape_df is not None and shape_pos_df is not None:
                # shape의 순차 연결 lines 생성
                if len(shape_df) > 1:
                    for i in range(len(shape_df) - 1):
                        from_coord = shape_df.iloc[i]
                        to_coord = shape_df.iloc[i + 1]
                        
                        # 해당 좌표에 해당하는 address 찾기
                        from_addr = addresses[
                            (addresses['pos'].apply(lambda pos: pos['x'] == from_coord['x'])) &
                            (addresses['pos'].apply(lambda pos: pos['y'] == from_coord['y'])) &
                            (addresses['pos'].apply(lambda pos: pos['z'] == from_coord['z']))
                        ].iloc[0] if len(addresses[
                            (addresses['pos'].apply(lambda pos: pos['x'] == from_coord['x'])) &
                            (addresses['pos'].apply(lambda pos: pos['y'] == from_coord['y'])) &
                            (addresses['pos'].apply(lambda pos: pos['z'] == from_coord['z']))
                        ]) > 0 else None
                        
                        to_addr = addresses[
                            (addresses['pos'].apply(lambda pos: pos['x'] == to_coord['x'])) &
                            (addresses['pos'].apply(lambda pos: pos['y'] == to_coord['y'])) &
                            (addresses['pos'].apply(lambda pos: pos['z'] == to_coord['z']))
                        ].iloc[0] if len(addresses[
                            (addresses['pos'].apply(lambda pos: pos['x'] == to_coord['x'])) &
                            (addresses['pos'].apply(lambda pos: pos['y'] == to_coord['y'])) &
                            (addresses['pos'].apply(lambda pos: pos['z'] == to_coord['z']))
                        ]) > 0 else None
                        
                        if from_addr is not None and to_addr is not None:
                            lines.append({
                                'id': self.line_id,
                                'name': f'LINE_{from_addr["id"]}_{to_addr["id"]}',
                                'fromAddress': from_addr['id'],
                                'toAddress': to_addr['id'],
                                'fromPos': from_addr['pos'],
                                'toPos': to_addr['pos'],
                                'curve': False
                            })
                            self.line_id += 1
                
                # shape_pos의 각 점에 대해 shape와 동일한 모양의 lines 생성
                if len(shape_pos_df) > 0 and len(shape_df) > 0:
                    # shape의 첫 번째 좌표를 원본 기준점으로 사용
                    original_base = shape_df.iloc[0]
                    original_x, original_y, original_z = original_base['x'], original_base['y'], original_base['z']
                    
                    # shape_pos_df의 각 점에 대해 반복
                    for pos_idx, pos_row in shape_pos_df.iterrows():
                        # 현재 shape_pos 점을 새로운 기준점으로 사용
                        base_x, base_y, base_z = pos_row['x'], pos_row['y'], pos_row['z']
                        
                        # offset 계산 (현재 기준점 - 원본 기준점)
                        x_offset = base_x - original_x
                        y_offset = base_y - original_y
                        z_offset = base_z - original_z
                        
                        # shape의 순차 연결과 동일한 패턴으로 lines 생성
                        if len(shape_df) > 1:
                            for i in range(len(shape_df) - 1):
                                from_coord = shape_df.iloc[i]
                                to_coord = shape_df.iloc[i + 1]
                                
                                # offset을 적용한 좌표 계산
                                from_x = from_coord['x'] + x_offset
                                from_y = from_coord['y'] + y_offset
                                from_z = from_coord['z'] + z_offset
                                to_x = to_coord['x'] + x_offset
                                to_y = to_coord['y'] + y_offset
                                to_z = to_coord['z'] + z_offset
                                
                                # 해당 좌표에 해당하는 address 찾기
                                from_addr = addresses[
                                    (addresses['pos'].apply(lambda pos: pos['x'] == from_x)) &
                                    (addresses['pos'].apply(lambda pos: pos['y'] == from_y)) &
                                    (addresses['pos'].apply(lambda pos: pos['z'] == from_z))
                                ].iloc[0] if len(addresses[
                                    (addresses['pos'].apply(lambda pos: pos['x'] == from_x)) &
                                    (addresses['pos'].apply(lambda pos: pos['y'] == from_y)) &
                                    (addresses['pos'].apply(lambda pos: pos['z'] == from_z))
                                ]) > 0 else None
                                
                                to_addr = addresses[
                                    (addresses['pos'].apply(lambda pos: pos['x'] == to_x)) &
                                    (addresses['pos'].apply(lambda pos: pos['y'] == to_y)) &
                                    (addresses['pos'].apply(lambda pos: pos['z'] == to_z))
                                ].iloc[0] if len(addresses[
                                    (addresses['pos'].apply(lambda pos: pos['x'] == to_x)) &
                                    (addresses['pos'].apply(lambda pos: pos['y'] == to_y)) &
                                    (addresses['pos'].apply(lambda pos: pos['z'] == to_z))
                                ]) > 0 else None
                                
                                if from_addr is not None and to_addr is not None:
                                    lines.append({
                                        'id': self.line_id,
                                        'name': f'LINE_{from_addr["id"]}_{to_addr["id"]}',
                                        'fromAddress': from_addr['id'],
                                        'toAddress': to_addr['id'],
                                        'fromPos': from_addr['pos'],
                                        'toPos': to_addr['pos'],
                                        'curve': False
                                    })
                                    self.line_id += 1
        

        
        return pd.DataFrame(lines)

    def make_lines_from_endpoint(self, addresses, lines):
        """endpoint를 연결하여 모든 address가 fromAddress와 toAddress에 각각 한 번 이상씩 나오도록 함"""
        print("4. endpoint 연결하여 모든 address가 fromAddress/toAddress에 포함되도록 함...")
        
        # 모든 address ID 수집
        all_address_ids = set(addr['id'] for addr in addresses.to_dict('records'))
        
        # 기존 lines에서 fromAddress와 toAddress 수집
        from_addresses = set()
        to_addresses = set()
        for _, line in lines.iterrows():
            from_addresses.add(line['fromAddress'])
            to_addresses.add(line['toAddress'])
        
        # 조건을 만족하지 못하는 address들을 endpoint로 정의
        # fromAddress나 toAddress에 한 번도 나오지 않는 address들
        isolated_endpoints = all_address_ids - from_addresses - to_addresses
        
        # fromAddress에만 나오거나 toAddress에만 나오는 address들도 endpoint로 정의
        from_only_endpoints = from_addresses - to_addresses
        to_only_endpoints = to_addresses - from_addresses
        
        # 모든 endpoint 수집
        all_endpoints = isolated_endpoints.union(from_only_endpoints).union(to_only_endpoints)
        
        print(f"   - 전체 address 수: {len(all_address_ids)}")
        print(f"   - fromAddress에 포함된 address 수: {len(from_addresses)}")
        print(f"   - toAddress에 포함된 address 수: {len(to_addresses)}")
        print(f"   - 고립된 endpoint 수: {len(isolated_endpoints)}")
        print(f"   - fromAddress에만 나오는 endpoint 수: {len(from_only_endpoints)}")
        print(f"   - toAddress에만 나오는 endpoint 수: {len(to_only_endpoints)}")
        print(f"   - 총 endpoint 수: {len(all_endpoints)}")
        
        if len(all_endpoints) == 0:
            print("   - 모든 address가 조건을 만족하므로 추가 line이 필요하지 않습니다.")
            return lines
        
        # 추가할 lines
        additional_lines = []
        all_addresses = addresses.to_dict('records')
        
        def find_nearest_address(target_addr_id, exclude_addr_ids=None):
            """주어진 address에서 가장 가까운 다른 address를 찾되, 특정 address ID들은 제외"""
            if exclude_addr_ids is None:
                exclude_addr_ids = set()
            
            target_addr = None
            for addr in all_addresses:
                if addr['id'] == target_addr_id:
                    target_addr = addr
                    break
            
            if not target_addr:
                return None
            
            min_dist = float('inf')
            nearest_addr = None
            for addr in all_addresses:
                if addr['id'] in exclude_addr_ids or addr['id'] == target_addr_id:
                    continue  # 제외할 address는 건너뛰기
                
                # 같은 라인(x, z 좌표가 동일)에 있는 address는 제외
                if (abs(target_addr['pos']['x'] - addr['pos']['x']) < 1e-6 and 
                    abs(target_addr['pos']['z'] - addr['pos']['z']) < 1e-6):
                    continue
                
                dist = math.sqrt((target_addr['pos']['x']-addr['pos']['x'])**2 + 
                               (target_addr['pos']['y']-addr['pos']['y'])**2 + 
                               (target_addr['pos']['z']-addr['pos']['z'])**2)
                if dist < min_dist:
                    min_dist = dist
                    nearest_addr = addr
            return nearest_addr
        
        # 기존 lines에서 이미 연결된 address 쌍들을 수집
        existing_connections = set()
        for _, line in lines.iterrows():
            # 양방향 연결을 고려하여 정렬된 쌍으로 저장
            addr_pair = tuple(sorted([line['fromAddress'], line['toAddress']]))
            existing_connections.add(addr_pair)
        
        # endpoint들을 가장 가까운 address와 연결 (겹치지 않게)
        for endpoint_id in all_endpoints:
            nearest_addr = find_nearest_address(endpoint_id)
            if nearest_addr:
                # 연결할 address 쌍
                connection_pair = tuple(sorted([endpoint_id, nearest_addr['id']]))
                
                # 이미 연결된 쌍인지 확인
                if connection_pair in existing_connections:
                    # 이미 연결되어 있으면 다른 address 찾기
                    exclude_ids = {endpoint_id, nearest_addr['id']}
                    nearest_addr = find_nearest_address(endpoint_id, exclude_ids)
                    if nearest_addr:
                        connection_pair = tuple(sorted([endpoint_id, nearest_addr['id']]))
                    else:
                        continue  # 다른 연결 가능한 address가 없으면 건너뛰기
                
                # 고립된 endpoint의 경우: endpoint -> nearest_address
                if endpoint_id in isolated_endpoints:
                    additional_lines.append({
                        'id': self.line_id,
                        'name': f'LINE_{endpoint_id}_{nearest_addr["id"]}',
                        'fromAddress': endpoint_id,
                        'toAddress': nearest_addr['id'],
                        'fromPos': next(addr['pos'] for addr in all_addresses if addr['id'] == endpoint_id),
                        'toPos': nearest_addr['pos'],
                        'curve': False
                    })
                    self.line_id += 1
                    existing_connections.add(connection_pair)
                
                # fromAddress에만 나오는 endpoint의 경우: nearest_address -> endpoint
                elif endpoint_id in from_only_endpoints:
                    additional_lines.append({
                        'id': self.line_id,
                        'name': f'LINE_{nearest_addr["id"]}_{endpoint_id}',
                        'fromAddress': nearest_addr['id'],
                        'toAddress': endpoint_id,
                        'fromPos': nearest_addr['pos'],
                        'toPos': next(addr['pos'] for addr in all_addresses if addr['id'] == endpoint_id),
                'curve': False
            })
                    self.line_id += 1
                    existing_connections.add(connection_pair)
                
                # toAddress에만 나오는 endpoint의 경우: endpoint -> nearest_address
                elif endpoint_id in to_only_endpoints:
                    additional_lines.append({
                        'id': self.line_id,
                        'name': f'LINE_{endpoint_id}_{nearest_addr["id"]}',
                        'fromAddress': endpoint_id,
                        'toAddress': nearest_addr['id'],
                        'fromPos': next(addr['pos'] for addr in all_addresses if addr['id'] == endpoint_id),
                        'toPos': nearest_addr['pos'],
                        'curve': False
                    })
                    self.line_id += 1
                    existing_connections.add(connection_pair)
        
        print(f"   - 추가된 line 수: {len(additional_lines)}")
        
        # 기존 lines와 추가 lines 합치기
        if additional_lines:
            all_lines = pd.concat([lines, pd.DataFrame(additional_lines)], ignore_index=True)
        else:
            all_lines = lines
        
        return all_lines






    def process_data(self, output_file=OUTPUT_FILE):
        """전체 데이터 처리 과정"""
        print("1. Input JSON 데이터 읽기...")
        x_axis_lines, y_axis_lines, shape1_df, shape1_pos_df, shape2_df, shape2_pos_df, shape3_df, shape3_pos_df, shape4_df, shape4_pos_df, shape5_df, shape5_pos_df, shape6_df, shape6_pos_df, shape7_df, shape8_df = self.read_input_json()
        
        print("2. Address 생성...")
        addresses_x = self.make_addresses(x_axis_lines)
        addresses_y = self.make_addresses(y_axis_lines)
        addresses_shape = self.make_addresses(pd.DataFrame(), shape1_df, shape1_pos_df, shape2_df, shape2_pos_df, shape3_df, shape3_pos_df, shape4_df, shape4_pos_df, shape5_df, shape5_pos_df, shape6_df, shape6_pos_df)
        
        # Area 라인 생성 및 address 생성 (x/y_axis_lines와 동일한 방식)
        print("2-1. Area 라인 생성...")
        area_lines_shape7 = self.generate_area_lines(shape7_df, shape7_df.iloc[0]['z']) if shape7_df is not None and len(shape7_df) > 0 else pd.DataFrame()
        area_lines_shape8 = self.generate_area_lines(shape8_df, shape8_df.iloc[0]['z']) if shape8_df is not None and len(shape8_df) > 0 else pd.DataFrame()
        
        print("2-2. Area Address 생성...")
        addresses_area7 = self.make_addresses(area_lines_shape7)
        addresses_area8 = self.make_addresses(area_lines_shape8)
        
        # 모든 address 합치기
        all_addresses = pd.concat([addresses_x, addresses_y, addresses_shape, addresses_area7, addresses_area8], ignore_index=True)
        
        print("3. Lines 생성 (step1)...")
        lines_x = self.make_lines_from_addresses(addresses_x, x_axis_lines)
        lines_y = self.make_lines_from_addresses(addresses_y, y_axis_lines)
        lines_shape = self.make_lines_from_addresses(all_addresses, pd.DataFrame(), shape1_df, shape1_pos_df, shape2_df, shape2_pos_df, shape3_df, shape3_pos_df, shape4_df, shape4_pos_df, shape5_df, shape5_pos_df, shape6_df, shape6_pos_df)
        
        # Area lines 생성 (x/y_axis_lines와 동일한 방식)
        print("3-1. Area Lines 생성...")
        lines_area7 = self.make_lines_from_addresses(addresses_area7, area_lines_shape7)
        lines_area8 = self.make_lines_from_addresses(addresses_area8, area_lines_shape8)
        
        # 모든 lines 합치기
        all_lines = pd.concat([lines_x, lines_y, lines_shape, lines_area7, lines_area8], ignore_index=True)

        # 4. y_axis_lines pair 처리
        print("4. y_axis_lines pair 처리...")
        pairs = self.find_y_line_pairs(y_axis_lines)
        print(f"   - 발견된 pair 수: {len(pairs)}")
        pair_lines = self.create_pair_lines(pairs, all_addresses)
        print(f"   - 생성된 pair line 수: {len(pair_lines)}")
        
        if pair_lines:
            all_lines = pd.concat([all_lines, pd.DataFrame(pair_lines)], ignore_index=True)

        # 5. endpoint 연결하여 모든 address가 fromAddress/toAddress에 포함되도록 함
        all_lines = self.make_lines_from_endpoint(all_addresses, all_lines)

        output = {
            'addresses': all_addresses.to_dict('records'),
            'lines': all_lines.to_dict('records'),
            'metadata': {
                'x_axis_addresses': len(addresses_x),
                'y_axis_addresses': len(addresses_y),
                'shape_addresses': len(addresses_shape),
                'total_addresses': len(all_addresses),
                'total_lines': len(all_lines),
                'shape1_coords': shape1_df.to_dict('records'),
                'shape1_pos_coords': shape1_pos_df.to_dict('records'),
                'shape2_coords': shape2_df.to_dict('records'),
                'shape2_pos_coords': shape2_pos_df.to_dict('records'),
                'shape3_coords': shape3_df.to_dict('records'),
                'shape3_pos_coords': shape3_pos_df.to_dict('records'),
                'shape4_coords': shape4_df.to_dict('records'),
                'shape4_pos_coords': shape4_pos_df.to_dict('records'),
                'shape5_coords': shape5_df.to_dict('records'),
                'shape5_pos_coords': shape5_pos_df.to_dict('records'),
                'shape6_coords': shape6_df.to_dict('records'),
                'shape6_pos_coords': shape6_pos_df.to_dict('records'),
                'shape7_coords': shape7_df.to_dict('records'),
                'shape8_coords': shape8_df.to_dict('records')
            }
        }
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
        print(f"5. 완료! {len(all_addresses)}개 address, {len(all_lines)}개 line이 {output_file}에 저장됨")
        return output 