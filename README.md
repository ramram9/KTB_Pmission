### OpenAI API를 사용하여 텍스트 생성 및 처리

OpenAI API를 사용한 텍스트 생성 및 처리 웹 애플리케이션입니다.
설치 및 설정
사전 요구사항

Python 3.8 이상
pip (Python 패키지 관리자)
OpenAI API 키

# 설치 방법

저장소 클론 또는 다운로드

bashCopygit clone [저장소 URL]
cd openai-project

Python 가상환경 생성 및 활성화

bashCopypython -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

필요한 패키지 설치

bashCopypip install flask openai python-dotenv

환경 변수 설정


.env 파일 생성
OpenAI API 키 추가:

CopyOPENAI_API_KEY=your-api-key-here
사용 방법

서버 실행

bashCopypython app.py

웹 브라우저에서 접속


http://localhost:5000 으로 접속
텍스트 입력 창에 프롬프트 입력
생성 버튼 클릭

# API 키 관리

OpenAI API 키 발급


OpenAI 웹사이트(https://platform.openai.com) 방문
계정 생성 또는 로그인
API 키 생성


API 키 보안


.env 파일은 절대 공개 저장소에 커밋하지 않기
.gitignore에 .env 추가

# 주요 기능

텍스트 생성
채팅 인터페이스
대화 기록 저장
<img width="912" alt="image" src="https://github.com/user-attachments/assets/b5c14b44-5b65-4e34-9b7d-b7172a0554b0">
