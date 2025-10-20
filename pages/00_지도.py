import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Seoul Travel Map", layout="wide")

st.title("🗺️ 외국인들이 좋아하는 서울의 주요 관광지 Top 10")
st.write("서울을 대표하는 인기 명소들을 지도에서 확인해보세요!")

# 관광지 데이터 (위도, 경도)
places = [
    {"name": "경복궁 (Gyeongbokgung Palace)", "lat": 37.579617, "lon": 126.977041},
    {"name": "명동 (Myeongdong)", "lat": 37.563757, "lon": 126.982669},
    {"name": "남산타워 (N Seoul Tower)", "lat": 37.551169, "lon": 126.988227},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", "lat": 37.582604, "lon": 126.983998},
    {"name": "홍대 (Hongdae)", "lat": 37.556343, "lon": 126.922651},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.566491, "lon": 127.009144},
    {"name": "청계천 (Cheonggyecheon Stream)", "lat": 37.569077, "lon": 126.982679},
    {"name": "롯데월드타워 (Lotte World Tower)", "lat": 37.513068, "lon": 127.102498},
    {"name": "이태원 (Itaewon)", "lat": 37.534799, "lon": 126.994593},
    {"name": "인사동 (Insadong)", "lat": 37.574006, "lon": 126.984961},
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for place in places:
    folium.Marker(
        [place["lat"], place["lon"]],
        popup=place["name"],
        tooltip=place["name"],
        icon=folium.Icon(color="green", icon="star")
    ).add_to(m)

# 지도 표시
st_data = st_folium(m, width=900, height=600)

st.write("💡 각 장소를 클릭하면 이름이 표시됩니다!")
st.write("✅ 데이터 출처: Visit Seoul, TripAdvisor, Google Maps")
