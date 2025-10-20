import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.colors as pc

# 페이지 설정
st.set_page_config(page_title="MBTI by Country", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 제목
st.title("🌍 국가별 MBTI 유형 비율 시각화")
st.write("국가를 선택하면 해당 국가의 16가지 MBTI 비율을 인터랙티브 그래프로 확인할 수 있습니다.")

# 국가 선택
country = st.selectbox("국가를 선택하세요:", df["Country"].sort_values())

# 선택한 국가 데이터 필터링
country_data = df[df["Country"] == country].iloc[0, 1:]  # 첫 번째 행, MBTI만
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "Percentage": country_data.values
}).sort_values("Percentage", ascending=False)

# 색상 처리: 1등은 빨간색, 나머지는 파랑 그라데이션
blue_scale = pc.sample_colorscale("Blues", [i / (len(country_df)-1) for i in range(len(country_df)-1)])
colors = ["#ff4b4b"] + blue_scale

# 그래프 그리기
fig = px.bar(
    country_df,
    x="MBTI",
    y="Percentage",
    title=f"🇨🇭 {country}의 MBTI 유형 비율",
    color="MBTI",
    color_discrete_sequence=colors,
    hover_data={"Percentage": ":.2%"},
)

fig.update_traces(
    hovertemplate="<b>%{x}</b><br>비율: %{y:.2%}",
    marker_line_color="white",
    marker_line_width=1.2
)

fig.update_layout(
    title_font_size=22,
    title_x=0.5,
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    plot_bgcolor="white",
    paper_bgcolor="white",
    showlegend=False,
    yaxis=dict(tickformat=".0%"),
)

st.plotly_chart(fig, use_container_width=True)

# 데이터표 표시 (옵션)
with st.expander("📊 원본 데이터 보기"):
    st.dataframe(country_df.style.format({"Percentage": "{:.2%}"}))
