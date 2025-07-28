# 데이터 처리 설정
LAYOUT_FILE = 'layout.json'
OUTPUT_FILE = 'output.json'
INPUT_FILE = 'input.json'

# ID 시작값 설정
ADDRESS_ID_START = 100001
LINE_ID_START = 200001

# 구간 설정
RANDOM_INTERVAL = [33.0, 44.0, 55.0, 66.0]

# y_axis_lines pair 설정
Y_LINE_PAIR_CONFIG = {
    'min_length': 1400,  # y line 최소 길이
    'mid_range_min': 3600,  # y line 중간값 최소
    'mid_range_max': 3800,  # y line 중간값 최대
    'pair_distance_min': 60,  # pair 간격 최소값
    'pair_distance_max': 100,  # pair 간격 최대값
    'y_near_3600': 3600,  # 3600 근처 값
    'y_near_3800': 3800,  # 3800 근처 값
    'near_tolerance': 50,  # 근처 판정 허용 오차
    
    # 5300~5500 범위 설정
    'mid_range_min_2': 5300,  # y line 중간값 최소 (두 번째 범위)
    'mid_range_max_2': 5500,  # y line 중간값 최대 (두 번째 범위)
    'y_near_5300': 5300,  # 5300 근처 값
    'y_near_5500': 5500,  # 5500 근처 값
}

# 시각화 설정
VISUALIZATION_WIDTH = 1920
VISUALIZATION_HEIGHT = 1080

# Z값별 색상
#  설정
Z_COLORS = {
    6022: '#ff4444',  # 빨간색
    4822: '#4444ff',  # 파란색
    'other': '#44ff44',  # 녹색 (기본)
    'default': '#44aaff'  # 기본 파란색
}

# 시각화 상세 설정
VISUALIZATION_CONFIG = {
    'marker_size': 3,
    'line_width': 1,
    'marker_border_color': None,
    'marker_border_width': 0,
    'hover_mode': 'closest',
    'legend_position': {
        'yanchor': 'top',
        'y': 0.99,
        'xanchor': 'left',
        'x': 0.01
    },
    'stats_annotation': {
        'bgcolor': 'rgba(255,255,255,0.8)',
        'bordercolor': 'black',
        'borderwidth': 1,
        'x': 0.02,
        'y': 0.98
    }
}

# Z값 필터링 설정
Z_VALUES = {
    'z6022': 6022,
    'z4822': 4822
}

# 시각화 표시 설정
VISUALIZATION_DISPLAY = {
    'show_both_windows': True,  # True: 두 창 모두 표시, False: 설정에 따라 하나만 표시
    'show_z6022_only': False,  # show_both_windows가 False일 때만 사용
    'title': 'Layout Visualization'  # 시각화 제목
}

# 파일 경로 설정
FILES = {
    'layout': 'layout.json',
} 