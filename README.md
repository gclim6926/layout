# Layout Generator

라인 데이터를 기반으로 address와 line을 생성하고 시각화하는 시스템입니다.

## 전체 구조

```
input.json → data_processor.py → layout.json → visualize2.py → 브라우저 시각화
```

## 파일 구조

### 1. 입력 파일

- **`input.json`**: 원본 라인 데이터 (x_axis_lines, y_axis_lines)
  - x/y_axis_lines: 주요 x,y축 라인
  - shape1,2 : z6022, 끝단의 이중 rail (shape1_pos는 동일형상 address 생성을 위한 기준좌표)
  - shape3,4 : z6022, 중심부 이중 rail로 z4822와 연결부분
  - shape5,6 : z4822, 외곽부 temp platform (동일 형상)
  - shape7,8 : z4822, 외곽부 big platform (해당 area에 임의의 x/y line 임의 생성)

### 2. 설정 파일

- **`config.py`**: 모든 설정값 관리
  - `LINE_RANDOM_INTERVAL`: address 생성 간격
  - `Z_COLORS`: Z값별 색상 설정
  - `VISUALIZATION_CONFIG`: 시각화 설정
  - `FILES`: 파일 경로 설정

### 3. 핵심 처리 파일

- **`data_processor.py`**: 데이터 처리 엔진
  - `read_input_lines()`: input.json에서 라인 데이터 읽기
  - `make_addresses()`: 라인을 따라 address 생성
  - `make_lines_from_addresses()`: address를 연결하는 line 생성
  - `process_data()`: 전체 처리 과정 실행

### 4. 출력 파일

- **`layout.json`**: 처리된 address와 line 데이터

### 5. 시각화 파일

- **`visualize2.py`**: layout.json을 읽어서 브라우저에서 시각화

### 6. 실행 파일

- **`main.py`**: 전체 프로세스 실행

## 실행 방법

```bash
python main.py
```

## 처리 과정

1. **데이터 읽기**: `input.json`에서 x_axis_lines, y_axis_lines 읽기
2. **Address 생성**: 각 라인을 따라 `LINE_RANDOM_INTERVAL` 간격으로 address 생성
3. **Line 생성**: 생성된 address들을 연결하는 line 생성
4. **저장**: 결과를 `layout.json`에 저장
5. **시각화**: `layout.json`을 읽어서 브라우저에서 시각화

## 데이터 구조

### Address

```json
{
  "id": 1,
  "address": 1,
  "name": "ADDR_1",
  "pos": {"x": 100, "y": 200, "z": 6022}
}
```

### Line

```json
{
  "id": 1,
  "name": "LINE_1_2",
  "fromAddress": 1,
  "toAddress": 2,
  "fromPos": {"x": 100, "y": 200, "z": 6022},
  "toPos": {"x": 150, "y": 250, "z": 6022},
  "curve": false
}
```
