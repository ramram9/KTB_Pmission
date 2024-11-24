from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

history = []

load_dotenv(override=True)  # 환경변수 로드
app = Flask(__name__) #웹 서버 애플리케이션 생성, 기본틀을 만드는 과정
openAI_key = os.getenv('OPENAI_API_KEY')
#OpenAI API 클라이언트 초기화 .env 파일에서 API키를 가져와 설정
client = OpenAI(api_key = openAI_key)

#메인 페이지 라우트
@app.route('/')
def home():
   return render_template('index.html')

# '/generate' 엔드포인트 정의 (POST 요청만 허용)
@app.route('/generate', methods=['POST'])
def generate_text():
    # POST 요청에서 JSON 데이터 추출
    data = request.json
    # 'prompt' 키로 전송된 텍스트 가져오기 (없으면 빈 문자열)
    prompt = data.get('prompt', '')

    # OpenAI API를 호출하여 텍스트 생성
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 사용할 AI 모델
        messages=[  # 대화 메시지 설정
            {
                "role": "system",
                "content": '''
                당신은 훌륭한 어시스턴트 입니다.
                당신은 텍스트 생성, 텍스트 요약, 텍스트 번역, 사용자 질문 응답 기능을 제공합니다. 
                항상 핵심만 간결하고 정확하게 제공합니다.'''
            },
            {

                "role": "user",  # 사용자 역할
                "content": prompt  # 사용자가 입력한 프롬프트
            }
        ]
    )
    result = response.choices[0].message.content

    history.append({
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'prompt': prompt,
        'response': result
    })
    # API 응답에서 생성된 텍스트 추출하여 JSON 형태로 반환
    return jsonify({
        "text": result
    })

#히스토리 조회 엔드포인트
@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(history)

# 메인 프로그램으로 실행될 때만 서버 시작
if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드로 서버 실행