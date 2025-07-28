import json
import plotly.graph_objects as go
import plotly.io as pio
from config import Z_COLORS, VISUALIZATION_CONFIG, Z_VALUES, FILES, VISUALIZATION_DISPLAY, VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT, LAYOUT_FILE

# plotly 브라우저 자동 열기 설정
pio.renderers.default = "browser"

# 전역 변수로 데이터 저장
addresses = []
lines = []
addresses_z6022 = []
lines_z6022 = []
addresses_not_z6022 = []
lines_not_z6022 = []

def load_data():
    """layout.json에서 데이터 로드 및 분리"""
    global addresses, lines, addresses_z6022, lines_z6022, addresses_not_z6022, lines_not_z6022
    
    with open(LAYOUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    addresses = data['addresses']
    lines = data['lines']
    
    # z값별로 데이터 분리
    addresses_z6022, lines_z6022 = filter_data_by_z(Z_VALUES['z6022'], include=True)
    addresses_not_z6022, lines_not_z6022 = filter_data_by_z(Z_VALUES['z6022'], include=False)

def get_color_by_z(z, green_for_non_4822=False):
    """Z값에 따른 색상 반환"""
    if z == Z_VALUES['z6022']:
        return Z_COLORS[Z_VALUES['z6022']]
    elif z == Z_VALUES['z4822']:
        return Z_COLORS[Z_VALUES['z4822']]
    else:
        return Z_COLORS['other'] if green_for_non_4822 else Z_COLORS['default']

def filter_data_by_z(z_value, include=True):
    """Z값에 따라 데이터 필터링"""
    if include:
        filtered_addresses = [a for a in addresses if a['pos']['z'] == z_value]
        filtered_lines = [l for l in lines if l['fromPos']['z'] == z_value or l['toPos']['z'] == z_value]
    else:
        filtered_addresses = [a for a in addresses if a['pos']['z'] != z_value]
        filtered_lines = [l for l in lines if l['fromPos']['z'] != z_value and l['toPos']['z'] != z_value]
    
    return filtered_addresses, filtered_lines

def create_visualization(addresses, lines, title, green_for_non_4822=False):
    """시각화 생성"""
    fig = go.Figure()
    
    # 선 그리기 - 벡터화된 방식으로 최적화
    if lines:
        # 모든 선의 좌표를 한 번에 추출
        x_coords = [[line['fromPos']['x'], line['toPos']['x']] for line in lines]
        y_coords = [[line['fromPos']['y'], line['toPos']['y']] for line in lines]
        z_coords = [[line['fromPos']['z'], line['toPos']['z']] for line in lines]
        
        # 색상 결정을 벡터화
        colors = []
        for z1, z2 in z_coords:
            if z1 == Z_VALUES['z6022'] or z2 == Z_VALUES['z6022']:
                colors.append(Z_COLORS[Z_VALUES['z6022']])
            elif z1 == Z_VALUES['z4822'] or z2 == Z_VALUES['z4822']:
                colors.append(Z_COLORS[Z_VALUES['z4822']])
            else:
                colors.append(get_color_by_z(z1, green_for_non_4822))
        
        # 모든 선을 한 번에 추가
        for i, line in enumerate(lines):
            fig.add_trace(go.Scatter(
                x=x_coords[i],
                y=y_coords[i],
                mode='lines',
                line=dict(color=colors[i], width=VISUALIZATION_CONFIG['line_width']),
                name=f'Line {line["id"]}',
                showlegend=False,
                hovertemplate=(
                    f'<b>{line["name"]}</b><br>'
                    f'fromAddress: {line["fromAddress"]}<br>'
                    f'toAddress: {line["toAddress"]}<extra></extra>'
                )
            ))
    
    # 점 그리기 - 벡터화된 방식으로 최적화
    if addresses:
        # 모든 좌표를 한 번에 추출
        x_coords = [addr['pos']['x'] for addr in addresses]
        y_coords = [addr['pos']['y'] for addr in addresses]
        colors = [get_color_by_z(addr['pos']['z'], green_for_non_4822) for addr in addresses]
        ids = [addr['id'] for addr in addresses]
        z_values = [addr['pos']['z'] for addr in addresses]
        
        fig.add_trace(go.Scatter(
            x=x_coords,
            y=y_coords,
            mode='markers',
            marker=dict(
                size=VISUALIZATION_CONFIG['marker_size'],
                color=colors,
                line=dict(color=VISUALIZATION_CONFIG['marker_border_color'], width=VISUALIZATION_CONFIG['marker_border_width'])
            ),
            name='Addresses',
            hovertemplate='<b>Address ID: %{text}</b><br>Position: (%{x:.2f}, %{y:.2f})<br>Z: %{customdata}<extra></extra>',
            text=ids,
            customdata=z_values,
            showlegend=False
        ))
    
    # 레이아웃 설정
    fig.update_layout(
        title=title,
        xaxis_title='X Coordinate',
        yaxis_title='Y Coordinate',
        hovermode=VISUALIZATION_CONFIG['hover_mode'],
        width=VISUALIZATION_WIDTH,
        height=VISUALIZATION_HEIGHT,
        showlegend=True,
        legend=dict(**VISUALIZATION_CONFIG['legend_position'])
    )
    
    # 범례 추가
    z_values_in_data = set(addr['pos']['z'] for addr in addresses)
    legend_items = []
    
    if Z_VALUES['z6022'] in z_values_in_data:
        legend_items.append(dict(name=f'z={Z_VALUES["z6022"]}', marker=dict(color=Z_COLORS[Z_VALUES['z6022']])))
    if Z_VALUES['z4822'] in z_values_in_data:
        legend_items.append(dict(name=f'z={Z_VALUES["z4822"]}', marker=dict(color=Z_COLORS[Z_VALUES['z4822']])))
    
    other_z_values = z_values_in_data - {Z_VALUES['z6022'], Z_VALUES['z4822']}
    if other_z_values:
        legend_name = 'z≠4822' if green_for_non_4822 else 'z≠6022'
        legend_color = Z_COLORS['other'] if green_for_non_4822 else Z_COLORS['default']
        legend_items.append(dict(name=legend_name, marker=dict(color=legend_color)))
    
    # 통계 정보 추가
    stats_text = f'Addresses: {len(addresses)}, Lines: {len(lines)}'
    fig.add_annotation(
        text=stats_text,
        xref="paper", yref="paper",
        showarrow=False,
        **VISUALIZATION_CONFIG['stats_annotation']
    )
    
    return fig

def print_address_info(addresses, title):
    """Address 정보 출력"""
    print("=" * 60)
    print(f"📋 {title}")
    print("=" * 60)
    print(f"총 Address 개수: {len(addresses)}")
    
    if not addresses:
        print("❌ 데이터가 없습니다.")
        return
    
    # Z값별 분포
    z_counts = {}
    for addr in addresses:
        z = addr['pos']['z']
        z_counts[z] = z_counts.get(z, 0) + 1
    
    print("\n📍 Z값별 분포:")
    for z, count in sorted(z_counts.items()):
        print(f"  z={z}: {count}개")
    
    # 처음 10개 Address 상세정보
    print(f"\n📝 처음 10개 Address 상세정보:")
    for i, addr in enumerate(addresses[:10], 1):
        pos = addr['pos']
        print(f"   {i:2d}. ID: {addr['id']} | Pos: ({pos['x']:.2f}, {pos['y']:.2f}, {pos['z']}) | Address: {addr['address']}")
    
    if len(addresses) > 10:
        print(f"  ... (총 {len(addresses)}개 중 10개만 표시)")
    
    # 좌표 범위
    x_coords = [addr['pos']['x'] for addr in addresses]
    y_coords = [addr['pos']['y'] for addr in addresses]
    z_coords = [addr['pos']['z'] for addr in addresses]
    
    print(f"\n🗺️  좌표 범위:")
    print(f"  X: {min(x_coords):.2f} ~ {max(x_coords):.2f} (범위: {max(x_coords) - min(x_coords):.2f})")
    print(f"  Y: {min(y_coords):.2f} ~ {max(y_coords):.2f} (범위: {max(y_coords) - min(y_coords):.2f})")
    print(f"  Z: {min(z_coords)} ~ {max(z_coords)}")

def create_visualizations():
    """시각화 생성 및 표시"""
    # 데이터 로드
    load_data()
    
    # Z=6022 시각화
    print("\n============================================================")
    print("📋 Z=6022 Address 정보")
    print("============================================================")
    print(f"총 Address 개수: {len(addresses_z6022)}")
    
    if addresses_z6022:
        print("\n📍 Z값별 분포:")
        z_counts = {}
        for addr in addresses_z6022:
            z = addr['pos']['z']
            z_counts[z] = z_counts.get(z, 0) + 1
        for z, count in sorted(z_counts.items()):
            print(f"  z={z}: {count}개")
        
        print(f"\n📝 처음 10개 Address 상세정보:")
        for i, addr in enumerate(addresses_z6022[:10], 1):
            pos = addr['pos']
            print(f"   {i:2d}. ID: {addr['id']} | Pos: ({pos['x']:.2f}, {pos['y']:.2f}, {pos['z']}) | Address: {addr['address']}")
        
        if len(addresses_z6022) > 10:
            print(f"  ... (총 {len(addresses_z6022)}개 중 10개만 표시)")
        
        # 좌표 범위
        x_coords = [addr['pos']['x'] for addr in addresses_z6022]
        y_coords = [addr['pos']['y'] for addr in addresses_z6022]
        z_coords = [addr['pos']['z'] for addr in addresses_z6022]
        
        print(f"\n🗺️  좌표 범위:")
        print(f"  X: {min(x_coords):.2f} ~ {max(x_coords):.2f} (범위: {max(x_coords) - min(x_coords):.2f})")
        print(f"  Y: {min(y_coords):.2f} ~ {max(y_coords):.2f} (범위: {max(y_coords) - min(y_coords):.2f})")
        print(f"  Z: {min(z_coords)} ~ {max(z_coords)}")
    
    # Z≠6022 시각화
    print("\n============================================================")
    print("📋 Z≠6022 Address 정보")
    print("============================================================")
    print(f"총 Address 개수: {len(addresses_not_z6022)}")
    
    if addresses_not_z6022:
        print("\n📍 Z값별 분포:")
        z_counts = {}
        for addr in addresses_not_z6022:
            z = addr['pos']['z']
            z_counts[z] = z_counts.get(z, 0) + 1
        for z, count in sorted(z_counts.items()):
            print(f"  z={z}: {count}개")
        
        print(f"\n📝 처음 10개 Address 상세정보:")
        for i, addr in enumerate(addresses_not_z6022[:10], 1):
            pos = addr['pos']
            print(f"   {i:2d}. ID: {addr['id']} | Pos: ({pos['x']:.2f}, {pos['y']:.2f}, {pos['z']}) | Address: {addr['address']}")
        
        if len(addresses_not_z6022) > 10:
            print(f"  ... (총 {len(addresses_not_z6022)}개 중 10개만 표시)")
        
        # 좌표 범위
        x_coords = [addr['pos']['x'] for addr in addresses_not_z6022]
        y_coords = [addr['pos']['y'] for addr in addresses_not_z6022]
        z_coords = [addr['pos']['z'] for addr in addresses_not_z6022]
        
        print(f"\n🗺️  좌표 범위:")
        print(f"  X: {min(x_coords):.2f} ~ {max(x_coords):.2f} (범위: {max(x_coords) - min(x_coords):.2f})")
        print(f"  Y: {min(y_coords):.2f} ~ {max(y_coords):.2f} (범위: {max(y_coords) - min(y_coords):.2f})")
        print(f"  Z: {min(z_coords)} ~ {max(z_coords)}")
    
    # 시각화 생성
    if VISUALIZATION_DISPLAY:
        # Z=6022 시각화
        if addresses_z6022 or lines_z6022:
            fig1 = create_visualization(addresses_z6022, lines_z6022, f'z={Z_VALUES["z6022"]} - {len(addresses_z6022)}개 주소, {len(lines_z6022)}개 선')
            fig1.show()
        
        # Z≠6022 시각화
        if addresses_not_z6022 or lines_not_z6022:
            fig2 = create_visualization(addresses_not_z6022, lines_not_z6022, f'z≠{Z_VALUES["z6022"]} - {len(addresses_not_z6022)}개 주소, {len(lines_not_z6022)}개 선', green_for_non_4822=True)
            fig2.show()
        
        print(f"\n🌐 두 개의 plotly figure가 각각 다른 브라우저 창에서 표시되었습니다.")
        print(f"창 1: z={Z_VALUES['z6022']} - {len(addresses_z6022)}개 주소, {len(lines_z6022)}개 선")
        print(f"창 2: z≠{Z_VALUES['z6022']} - {len(addresses_not_z6022)}개 주소, {len(lines_not_z6022)}개 선")
    else:
        print("\n❌ 시각화가 비활성화되어 있습니다. config.py에서 VISUALIZATION_DISPLAY를 True로 설정하세요.") 