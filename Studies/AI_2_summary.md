이 문서는 AI 2 과목을 정리해서 요약해 놓은 문서임.  
차후 Gemini canvas의 퀴즈 내용으로 입력할 예정임.

# 실습 1
## Step7: API와 HTTP - requests
- 주제: API 요청과 응답
- API는 프로그램끼리 요청과 응답을 주고받는 약속임.
- API 문서: 보낼 수 있는 요청의 종류와 형식을 정의
- 요청 (Request): 클라이언트가 서버로 보내는 메시지
- 응답 (Response): 서버가 돌려주는 결과
- 우리 코드(클라이언트)는 요청을 보내고 응답을 받는다.
- HTTP 메서드
  - GET: 데이터를 가져올 때 / 조회할 대
  - POST: 데이터를 보낼 때 (본문에 JSON)  / LLM 호출할 때
- 상태 코드: 요청 처리 결과를 나타내는 숫자 (200, 404, 500 등) / 첫 자리 숫자로 종류가 나뉜다.
- **`response` 객체의 주요 속성**

| 속성 | 타입 | 의미 |
| --- | --- | --- |
| `.status_code` | `int` | HTTP 상태 코드 (예: `200`) |
| `.text` | `str` | 응답 본문 (원본 **문자열**) |
| `.json()` | 메서드 | 본문을 파이썬 `dict`, `list`로 변환 |
| `.headers` | `dict` | 응답 헤더 |
| `.elapsed` | `timedelta` | 요청부터 응답까지 걸린 시간 |
| `.url` | `str` | 실제 요청된 URL |  

`.text`는 문자열이므로 `["name"]`처럼 키로 접근할 수 없습니다. JSON 응답을 파이썬 객체로 다룰 때는 `.json()`을 사용합니다.  
  
**예외 처리**: 네트워크 요청은 여러 이유로 실패합니다. 예외 원인에 따라 구분해 처리합니다.

| 예외 | 상황 |
| --- | --- |
| `requests.exceptions.Timeout` | 지정한 시간 안에 응답이 없음 |
| `requests.exceptions.ConnectionError` | 서버 연결 실패 |
| `requests.exceptions.HTTPError` | `raise_for_status()`가 `4xx`, `5xx` 상태를 감지 |
| `json.JSONDecodeError` | 응답이 유효한 JSON 이 아님 |

#### 실습 문제
### TODO 11: `GET` 요청과 `.json()` 변환

**요구사항**
- `try` 블록의 세 줄을 채워 API 를 호출하고 본문을 파이썬 객체로 바꿉니다.

**제한조건**
- 정답 확인용 `assert` 줄은 수정하지 않습니다.
- 세 줄 중 어디서든 실패하면 원인별 `except` 로 떨어져 샘플 데이터(`SAMPLE_USERS`)를 사용합니다. (네트워크가 막혀도 정상)

**힌트**
- 요청 `requests.get(API_URL, timeout=5)` 을 response 에 받습니다.
- 상태 코드 확인 `response.raise_for_status()`, 본문 변환 `response.json()`.
```python
import requests
import json

try:
    # 1. API_URL 로 GET 요청을 보내 response 에 받아 주세요. (timeout=5)
    API_URL = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(API_URL , timeout=5)   # 5초만에 응답 안해주면 Timeout 에러 발동
    # 2. 상태 코드가 200대가 아니면 예외를 일으켜 주세요.
    response.raise_for_status()   # raise_for_status()는 200번대 상태 코드(정상)이 아니면 에러를 띄우는 친구다.
    # 3. 응답 본문을 파이썬 객체로 바꿔 data 에 받아 주세요.
    data = response.json()   # 통문짜를 파이썬 객체로 바꿈(리스트, 딕셔너리)
    source = "API"
    print("상태 코드:", response.status_code, "| 소요 시간:", response.elapsed.total_seconds(), "초")
except requests.exceptions.Timeout:
    print("5초 내 응답 없음 , 샘플 데이터로 진행")
    data, source = SAMPLE_USERS, "SAMPLE"
except requests.exceptions.ConnectionError:
    print("네트워크 연결 실패 (서버 연결 실패) , 샘플 데이터로 진행")
    data, source = SAMPLE_USERS, "SAMPLE"
except requests.exceptions.HTTPError as e:
    print("HTTP 오류:", e, ", 샘플 데이터로 진행")
    data, source = SAMPLE_USERS, "SAMPLE"
except json.JSONDecodeError:
    print("응답이 유효한 JSON 이 아님 , 샘플 데이터로 진행")
    data, source = SAMPLE_USERS, "SAMPLE"

print("데이터 출처:", source, "| 사용자 수:", len(data))

assert isinstance(data, list) and len(data) >= 1, "data 가 리스트가 아니거나 비어 있습니다."
assert isinstance(data[0], dict), "data 의 원소가 dict 가 아닙니다."
assert "name" in data[0] and "email" in data[0], "사용자 dict 에 name/email 이 없습니다."
print("TODO 11 통과!")
```
## Step 8: JSON 파싱과 `DataFrame` 변환

### Concept Check: JSON 과 파이썬 자료형의 대응

JSON은 프로그램끼리 데이터를 주고받을 때 사용하는 텍스트 기반 형식이며, 파이썬 자료형과 다음처럼 대응합니다.

| JSON | 파이썬 | 접근 방법 |
| --- | --- | --- |
| `{ ... }` | `dict` | `d["key"]` |
| `[ ... ]` | `list` | `l[0]` |
| `"text"` | `str` | |
| `10`, `true` | `int`, `bool` | |
| `null` | `None` | |

API 응답은 보통 `dict` 안에 `dict`, `list` 안에 `dict` 처럼 **중첩(nested)** 돼 있습니다. 중첩 접근 방법은 Step 3 과 같습니다. **바깥쪽부터 안쪽까지** 키와 인덱스에 순서대로 접근합니다.

```python
data[0]["address"]["city"]
# list 의 0번 , dict 의 "address" , 다시 dict 의 "city"
```

**`d["key"]` vs `d.get("key")`**
- `d["key"]` - 키가 없으면 `KeyError` 로 멈춤. **반드시 있어야 하는** 키에 사용.
- `d.get("key")` - 없으면 `None` 반환. **없을 수도 있는** 선택적 필드에 사용.

API 응답은 사용자마다 일부 필드가 빠질 수 있으니, 선택적 필드에는 `get`을 사용합니다. `list` 인덱스도 범위를 벗어나면 `IndexError` 가 나므로 길이를 먼저 확인합니다.
```python
# 값을 꺼내기 전에 키가 어디 있는지 눈으로 확인하는 습관
first = data[0]
print("최상위 키:", list(first.keys()))
print("address 키:", list(first["address"].keys()))
print("company 키:", list(first["company"].keys()))
```
### TODO 12: 중첩 구조에서 값 꺼내기

**요구사항**
- 첫 번째 사용자(`data[0]`)에서 이름, 이메일, 도시, 회사명, 웹사이트를 꺼냅니다.

**제한조건**
- 정답 확인용 `assert` 줄은 수정하지 않습니다. `None` 자리만 채웁니다.

**힌트**
- 도시, 회사명은 한 단계 더 들어간 중첩 값입니다: `first["address"]["city"]`, `first["company"]["name"]`.
- 웹사이트는 없을 수도 있으니 `first.get("website")` 를 씁니다.
```python
first = data[0]

# 1. 이름을 first_name 에 할당해 주세요.
first_name = first["name"]
assert first_name == "Leanne Graham", "이름이 올바르지 않습니다."

# 2. 이메일을 first_email 에 할당해 주세요.
first_email = first["email"]
assert "@" in first_email, "이메일이 올바르지 않습니다."

# 3. 도시를 first_city 에 할당해 주세요.
first_city = first["address"]["city"]
assert first_city == "Gwenborough", "도시가 올바르지 않습니다."

# 4. 회사명을 first_company 에 할당해 주세요.
first_company = first["company"]["name"]
assert first_company == "Romaguera-Crona", "회사명이 올바르지 않습니다."

# 5. 웹사이트를 first.get 으로 website 에 할당해 주세요.
website = first.get("website", "기본값")
assert website == "hildegard.org", "웹사이트가 올바르지 않습니다."
assert first.get("없는키", "기본값") == "기본값", "get 의 기본값 동작을 확인하세요."

print("TODO 12 통과!")
```