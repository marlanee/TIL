# 복잡한 자료구조
### 문제
- 복잡한 자료구조 속에서, data 변수에 할당된 값을 찾아 value에 할당하는 문제

```python
data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
```

### 부족한 점
- 각 변수가 list인지 dict인지 판단하는 능력 부족
- list와 dict를 호출하는 방법 미숙
- 변수를 형변환 하는 기술 미숙

### 보완한 점
- dict 변수 내에서도 int 함수 사용
- dict 변수 하나를 특정해 f-string 사용
```python
first_data = {'제목': first_key, '일차': int(second_key), '단계': f"{third_key}단계", '과목': fourth_key}
```
### 소감
type을 정확히 파악하고 변수를 형변환하는 연습이 필요해 보인다.