### 2-2 로지스틱 회귀
1. 선형회귀를 분류 문제에 사용시, 범주의 순서를 인위적으로 암시하게 된다.
2. 로지스틱 회귀 모형은 입력 X에서 Y = 1이 될 확률을 의미한다.
### 2-3 신경망 모델
1. Shallow Network: 은닉층이 1개인 구조다. / Deep network는 이놈이 연속함수처럼 되어있는 구조
2. 신경망 모델은 각 은닉층에 활성화 함수를 적용하는 단계가 필수다.
3. Deep network는 최고다. 모든 수식을 포함한다.
### 2-4 신경망 적합
1. 경사 하강법의 파라미터 갱신 수식: `seta - a(미분값)`
2. Convex 문제는 2차 미분이 모든 구간에서 0 이상인 양수이다.
3. 경사 하강법의 step1 은 파라미터의 기울기를 계산하는게 우선이다. / 학습 전 딱 한번만 파라미터 초기화 진행
### 3-1 워드 임베딩
1. Skip-gram: 중심 단어로 주변 단어 예측 / CBOW는 빠르지만 데이터가 적을 때 효과적
2. 언어모델: 단방향 FNN -> RNN(순차 벡터 적용) 이미지: CNN
### 3-2 자연어 생성 모델
1. Attention 메커니즘의 필요성이 아닌 것: 입력을 작은 단위로 나누어 병렬 처리
2. BLEU: 기계번역의 결과가 인간 번역과 얼마나 유사한지 정량적으로 평가하는 지표
3. Attetion이 등장한 이유: Seq2Seq이 병목 현상(Bottleneck Problem)으로 입력 정보를 하나로 압축하며 정보를 손실시켜서.
### 3-3 Transformer
1. Decorder는 미래 단어 참조를 막기 위해 masking self-attention을 사용한다.
2. Multi-Headed Attention은 문자를 유형별로 묶을 수 있게 해준다.
3. Attetion 출력만으로는 너무 선형적이다 -> Feed-forward network 도입으로 비선형 변환 추가
### 3-4 사전 학습 기반 언어 모델
1. 모든 모델이 Encoder-Decoder 구조가 아니다.
  1. BERT: 인코더만 보유 / 판별 역할
  2. GPT: 디코더만 보유 / 입력 정보가 디코더로 직행
  3. FastText: 둘 다 안 가짐
  4. T5: 인디코더 보유
2. T5은 Span Corruption 방식을 사용한다.
  1. Mask처럼 하되, 단어 여러개를 가리는 것임
### 4-1 텍스트 파운데이션 살펴보기
1. 별 것 없음
### 4-2 거대 언어 모델의 학습
1. 지시 학습: 다양한 NLP 테스크를 지시-응답의 형태로 하나의 모델로 수행 가능하게 만듦
### 4-3 거대 언어 모델의 추론
1. Top-K, Top-P Sampling
2. 자동회귀 생성 방식: 입력된 토큰 시퀀스의 다음 토큰의 확률 분포를 예측하고 반복해서 응답을 생성함
### 4-4 거대 언어 모델의 평가
1. LLM 평가 요소: 목표, 평가 방법, 평가 지표
2. 텍스트 품질 평가 지표: ROUGE, Perplexity(PPL), 코사인 유사도
3. LLM-as-judge: 각종 편향이 있을 수 있다. / 데이터 증강도 만능은 아님
4. JSON: 데이터 파싱 및 구조화 최적화 라이브러리
5. Self-instruct AIpagasus: 인스트럭션 -> 분류 -> 인스턴스 -> 분류
### 5-1 이미지 딥러닝 모델
1. CNN은 2차원 구조(행렬)로 받아들여 지역 특징을 추출한다
2. Alexnet -> VG -> Googlenet -> resnet -> mobilenet
3. Resnet의 잔차 연결은 기울기 소실 문제를 안정화한다.
4. Mobilenet의 혁신적인 구조: 각 채널마다 별도의 합성곱
5. 풀링 레이어, 스트라이드 합성곱
6. VGGNet: 3x3 합성곱을 반복한게 특징
### 5-2 다양한 신경망 모델
1. RNN의 한계: 기울기 소실, 폭발
2. 지식 증류: 선생님 모델의 예측을 학생 모델이 모방함
3. 지식 증류는 데이터가 적을 때에도 강점을 발휘한다.
### 5-3 이미지 모델 학습 전략
1. Leaky ReLU: relu와 다르게 음수가 들어와도 0 이상의 숫자로 미분값을 남김. 기울기 소실을 차단
2. 계단식 학습률 감소 방식은 곡선이 불안정할 수 있다.
3. ResNet의 전처리 방법: 각 채널의 평균을 빼고 표준편차로 나누기
4. Linear Probing: 마지막 레이어만 학습한다.(선형 프로빙)
### 6-1 AI 파운데이션 모델
1. ViT 이미지를 1D로 flatten하고 position embedding을 사용함
2. CLIP은 이미지와 텍스트 쌍의 임베딩을 가까워지게 만든다.
3. CLIP의 로스 함수: 이미지와 텍스트의 코사인 유사도를 밀접하게 만든다. 양성-가깝게, 음성-멀게
4. 파운데이션 모델의 두드러지는 장점은, 다양한 태스크를 zero shot 등으로 사용 가능하다.
### 6-2 Vision-Language Model
1. VLM: Vision Encoder + Language Model
2. LLaVA는 적은 파라미터만을 학습 가능함
3. Qwen-VL은 유감스럽게도 3D 모델 디자인은 못함
4. 멀티모달 정합 손실함수: CLIP Loss
5. VLM은 DNA 염기서열 분석은 못함
### 6-3 Small VLM과 파운데이션 모델
1. Latent Diffusion Model(LDM): 저차원 latent 공간으로 연산 효율 향상
2. SAM: 다양한 입력으로 이미지의 임의 영역을 마스크 추출 / 영상 생성은 못 함
3. SoM: 객체 식별 성능 높인 녀석
### 6-4 개인화, 합성 데이터 활용
1. 파운데이션 모델은 특정 도메인에 적응할 시간이 필요하다
2. PEFT: 모델 전체가 아닌, 추가 학습 모듈 등 일부 파라미터만 학습
3. Gradio: ML모델을 웹 인터페이스로 쉽게 배포하는 도구
### 7-1 LangChain : Post-training
1. Pre-training: 대용량 데이터로 언어 구조 학습
   1. 다음 단어 예측에도 초점을 둔다.
2. Post-training: 사람의 의도와 요구에 맞게 모델 조정
3. Instruction-tuning: 지시문-응답 쌍으로 모델 미세조정
4. RLHF: 사람 피드백 반영
5. DPO: 강화학습 단계 삭제, 사람 선호 데이터 직접 활용
### 7-2 Retrieval-augmented LM(RAG)
1. RALM: 외부 데이터 저장소 활용(WEB) 추론
2. IR: IR의 목적은 검색 질의와 관련성이 가장 높은 정보 제공
3. Bi-encoder / Cross-encoder
   1. Bi-encoder: 별도 임베딩, 빠른 탐색
   2. Cross-encoder: 통합 입력, 높은 정확도
4. Sparse Retriever: 의미적 유사성보다 어휘적 매칭에 강함
5. Dense Retriever(임베딩 기반 탐색)
   1. 장점: 의미적 유사성 / 동의어, 다양한 표현 효과적 처리
### 7-3 LLMs with Tool Usage
1. Tool Learning: 도구 사용 학습 특화 훈련 필요
2. Toolformer 순서: 샘플링 -> API 실행 -> 필터링 -> 데이터셋 생성
3. MCP의 두 Layer
   1. Data Layer: JSON 메시지 형식 및 리소스
   2. Transport Layer: 실제 데이터 전송 담당
4. ToolLLM: 별도 튜닝 학습이 필요
5. 웹 에이전트(Web Shepherd)
   1. 주요 요소가 아닌 것: 사용자 질의에 대한 사전 정의된 정답
### 7-4 AI Agents & Langchain
1. Local Planning / Global Planning
   1. Local: 단계별 하나의 툴만 결정
   2. Global: 전체 경로 설계
2. LangCahin: LLM, DB, 외부 도구 등 다양한 요소 연결
## 8-1 Agent 모델: Introduction to AI Agent
1. AI agent: 추론하며 도구도 쓰는 그런 아이
### 8-2 Multi-Agent System
1. 다중 에이전트 시스템 구성 요소
   1. 아닌 것: 데이터베이스
2. 다중 에이전트 협업의 반복적 의사결정
   1. 과정에 포함되지 않는 단계: 데이터 삭제
3. MCP(모델 컨텍스트 프로토콜): 표준화로 도구 간 연결 복잡도 M * N -> M + N으로 낮춤
4. Toolformer
   1. 주요 특징이 아닌 것: 인간 개입 없이 모델 자체가 API 호출
5. Search-R1 접근법의 GRPO: 여러 실행 결과 비교, 상대적 우수 응답에 보상 부여
### 8-3 Memory & Tool in Multi Agent
1. 강화학습(RL) 사용 LLM의 예시가 아닌 것: VectorDB
### 8-4 Reasoning and Planning in AI
1. LLM 에이전트의 계획 수립 기법
   1. 해당되지 않는 것: Chain-of-Thought(tot) Prompting