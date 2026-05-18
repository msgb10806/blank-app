import streamlit as st

# 앱 제목 설정
st.title("가장 큰 수 찾기 앱")

# 1. 기존 input()을 st.number_input()으로 변경 (기본값은 0으로 설정)
num1 = st.number_input("첫번째 수:", value=0)
num2 = st.number_input("두번째 수:", value=0)
num3 = st.number_input("세번째 수:", value=0)

# 2. 기존 조건문 로직 (원본 그대로 유지)
if num1 > num2:
    if num3 > num1:
        st.write(f"결과: **{num3}**")  # print() 대신 웹 화면에 출력하는 st.write() 사용
    else:
        st.write(f"결과: **{num1}**")
else:
    if num3 > num2:
        st.write(f"결과: **{num3}**")
    else:
        st.write(f"결과: **{num2}**")