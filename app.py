import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="HBK AI Intelligence",
    page_icon="🤖",
    layout="centered"
)

# 다크 글래스 룩에 어울리도록 Streamlit 기본 여백 및 배경 다듬기
st.markdown("""
    <style>
    .stApp {
        background-color: transparent;
    }
    #MainMenu, footer, header {visibility: hidden;}
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

# 사용자 입력 받기 (Streamlit 하단 고정 채팅창)
if prompt := st.chat_input("예) 쇼핑몰 제작 비용과 구조가 궁금해요"):
    # 사용자 메시지 화면에 추가
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    user_query = prompt.strip().lower()
    
    # 💡 키워드별 풍부한 아키텍트 답변 데이터베이스
    answer = "HBK는 30년 경력의 시니어 아키텍트가 직접 비즈니스와 시스템을 진단합니다. 구체적인 요건을 남겨주시면 최적의 아키텍처를 제안해 드립니다."
    
    if any(k in user_query for k in ["비용", "견적", "얼마", "가격", "예산", "금액", "단가"]):
        answer = "프로젝트 예산은 요구하시는 기능 정의, 디자인 퀄리티(애플 스타일 글래스모피즘 등), 그리고 모듈 구성에 따라 상이합니다. 우측 상단의 '프로젝트 견적·상담'을 통해 상세 내용을 남겨주시면 정밀 진단해 드립니다."
    elif any(k in user_query for k in ["기술", "스택", "언어", "프레임워크", "리액트", "react", "파이썬", "python", "php", "자바", "spring"]):
        answer = "주로 React (Vite, Next.js) 기반의 하이엔드 프론트엔드와 Python FastAPI, Java Spring Boot, PHP 백엔드를 활용하며, Docker 및 Naver Cloud Platform(NCP) 기반의 안정적인 인프라를 구축하고 있습니다."
    elif any(k in user_query for k in ["기간", "일정", "얼마나 걸", "소요", "제작 기간", "날짜"]):
        answer = "표준 랜딩 페이지나 포트폴리오 사이트는 약 1~2주, 기능성 웹 애플리케이션 및 플랫폼 구축은 기획 범위에 따라 3~6주 정도의 소요 시간이 예상됩니다."
    elif any(k in user_query for k in ["대표", "hbk", "경력", "작업자", "아키텍트", "회사", "소개", "heartbreakkid"]):
        answer = "HBK(HeartBreakKid)는 약 30년 경력의 소프트웨어 아키텍트 및 풀스택 개발자가 운영하는 전문 웹 에이전시입니다(http://heartbreakkid.co.kr). 고품질의 SOLID 원칙 아키텍처와 애플 스타일의 감각적인 UI를 지향합니다."
    elif any(k in user_query for k in ["유지보수", "관리", "수정", "에러", "버그", "A/S"]):
        answer = "프로젝트 완료 후 철저한 안정화 기간을 거치며, 서버 모니터링, 백업 시스템 구축 및 지속적인 고도화 유지보수 서비스도 유연하게 지원하고 있습니다."
    elif any(k in user_query for k in ["디자인", "UI", "UX", "글래스모피즘", "모바일", "반응형", "앱"]):
        answer = "애플 스타일의 미니멀 다크 테마, 글래스모피즘 UI, 그리고 완벽한 모바일 반응형 내비게이션을 적용하여 시각적 몰입도가 높은 하이엔드 웹·앱 인터페이스를 구현합니다."
    elif any(k in user_query for k in ["서버", "배포", "인프라", "클라우드", "도메인", "호스팅", "ssl", "ncp", "docker"]):
        answer = "Naver Cloud Platform(NCP) 인프라 구축, 스테이징/프로덕션 환경 분리, Docker 컨테이너 세팅, SSL 인증서 통합 및 자동 DB 백업 시스템까지 완벽하게 엔지니어링합니다."
    elif any(k in user_query for k in ["연락", "상담", "문의", "전화", "이메일", "미팅"]):
        answer = "사이트 상단의 '프로젝트 견적·상담' 버튼을 통해 문의 양식을 남겨주시거나, 홈페이지 내 안내된 채널로 연락 주시면 신속하게 검토 후 회신해 드립니다."
    elif any(k in user_query for k in ["안녕", "반가워", "하이", "헬로", "반가워요"]):
        answer = "안녕하세요! HBK 시니어 아키텍트 AI입니다. 웹 제작, 기술 스택, 시스템 아키텍처에 대해 무엇이든 편하게 물어보세요."

    # AI 답변 출력 및 저장
    with st.chat_message("assistant"):
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
