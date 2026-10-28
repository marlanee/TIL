"""SWEA 14613 [Pro] 리스트 복사 — 직접 구현할 Python 학습 템플릿.

공식 Python 제출 양식이 아니라 공개 C++/Java API의 Python 대응이다.
이름은 널 문자 없는 str, mCopy는 bool, 인덱스는 0부터 시작한다.
입력/출력은 main.py가 담당한다. 여기에는 풀이 코드가 없다.
"""

# 26. 10. 28.
# SWEA 14613. [Pro] 리스트 복사
# 1차 시도: 09:37

"""
목표: 
"""
class Group:
    def __init__(self, root, length):
        self.root = root
        self.length = length

class Version:
    def __init__(self, parent=None, index=None, value=None, data=None):
        self.parent = parent
        self.index = index
        self.value = value
        self.data = data

class Node:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value
        
lists = {}  # 딕셔너리로 설정 / 리스트 이름과 데이터 연결엔 딕셔너리가 적합

def init() -> None:
    global lists
    lists = {}  # 상태 초기화

def makeList(mName: str, mLength: int, mListValue: list[int]) -> None:
    root = build(mListValue, 0, mLength - 1)
    lists[mName] = Group(root, mLength)

def copyList(mDest: str, mSrc: str, mCopy: bool) -> None:
    # mSrc는 str인데 왜 리스트가 생성되어 있음이 보장된다는거지?
    src = lists[mSrc]

    if mCopy:
        lists[mDest] = Group(src.root, src.length)
    else:
        lists[mDest] = src

def updateElement(mName: str, mIndex: int, mValue: int) -> None:
    group = lists[mName]

    group.root = update(
        group.root, 0, group.length - 1,
        mIndex, mValue
    )


def element(mName: str, mIndex: int) -> int:
    group = lists[mName]

    return query(
        group.root, 0, group.length - 1, mIndex
    )

# 수정 함수
def update(node, start, end, index, value):
    if start == end:
        return Node(value=value)

    mid = (start + end) // 2

    if index <= mid:
        new_left = update(node.left, start, mid, index, value)

        return Node(left=new_left, right = node.right)
    else:
        new_right = update(node.right, mid + 1, end, index, value)

        return Node(left = node.left, right = new_right)


def build(arr, start, end):
    if start == end:
        return Node(value=arr[start])

    mid = (start + end) // 2

    return Node(
        left=build(arr, start, mid),
        right=build(arr, mid + 1, end)
    )

def query(node, start, end, index):
    # 리프 노드에 도달하면 값 반환
    if start == end:
        return node.value

    mid = (start + end) // 2

    if index <= mid:
        return query(node.left, start, mid, index)
    else:
        return query(node.right, mid + 1, end, index)