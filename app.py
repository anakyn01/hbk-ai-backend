import streamlit as st
import os

# 페이지 설정 (애플 스타일 다크 테마 감성)
st.set_page_config(
    page_title="HBK AI Intelligence",
    page_icon="🤖",
    layout="centered"
)

# 커스텀 CSS로 다크 글래스룩 스타일링 살짝 가미
st.markdown("""
    <style>
    .main {
        background-color: #0e0e12;
        color: #ffffff;
    }
    .stTextInput input {
        background-color: rgba(255, 255, 255, 0.08);
        color: white;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 HBK 시니어 아키텍트 AI")
st.caption("웹 제작, 기술 스택, 예상 아키텍처에 대해 무엇이든 물어보세요.")

# 세션 스테이트로 대화 기록 유지
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "안녕하세요! HBK 시니어 아키텍트 AI입니다. 어떤 웹 비즈니스를 구상하고 계신가요?"}
    ]

# 이전 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력 받기
if prompt := st.chat_input("예) 쇼핑몰 제작 비용과 대략적인 구조가 궁금해요"):
    # 사용자 메시지 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI 응답 로직 (추후 OpenAI API 키를 환경 변수로 연동 가능)
    # 예: OpenAI 클라이언트 호출 코드 넣기
    response_text = "HBK는 30년 경력의 시니어 아키텍트가 직접 비즈니스 로직을 진단합니다. 기획 범위와 기능에 따라 맞춤형 아키텍처를 제안해 드립니다."

    if "비용" in prompt or "얼마" in prompt:
        response_text = "프로젝트 예산은 요구하시는 기능 정의와 모듈 구성에 따라 상이합니다. 우측 상단의 '프로젝트 견적·상담'을 통해 상세 내용을 남겨주시면 정밀 진단해 드립니다."
    elif "기술" in prompt or "스택" in prompt:
        response_text = "주로 React(Vite), Next.js, PHP, Python, Docker 기반의 안정적인 풀스택 환경을 구축하고 있습니다."

    # AI 답변 추가
    with st.chat_message("assistant"):
        st.markdown(response_text)
    st.session_state.messages.append({"role": "assistant", "content": response_text})