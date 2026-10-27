soldiers = {}
head = [[0] * 6 for _ in range(6)]
tail = [[0] * 6 for _ in range(6)]
next = [0]
node_soldier = [0]
def init():
    # 테스트 케이스 초기화
    global head, tail, next, node_soldier

    soldiers.clear()
    head = [[0] * 6 for _ in range(6)]
    tail = [[0] * 6 for _ in range(6)]
    next = [0]
    node_soldier = [0]
    return


def hire(mID, mTeam, mScore):
    # 병사 고용
    node = len(next)
    next.append(0)
    node_soldier.append(mID)

    soldiers[mID] = (mTeam, node)

    if head[mTeam][mScore] == 0:
        head[mTeam][mScore] = node
        tail[mTeam][mScore] = node

    else:
        last = tail[mTeam][mScore]
        next[last] = node
        tail[mTeam][mScore] = node


def fire(mID):
    # 병사 해고
    soldiers.pop(mID)


def updateSoldier(mID, mScore):
    # 병사 한 명의 평판 점수 변경
    team, old_node = soldiers[mID]
    hire(mID, team, mScore)

# 그룹을 점수 단위로 이동시키는 보조 함수
def move_group(team, src, dst):

    if src == dst or head[team][src] == 0:
        return

    src_head = head[team][src]
    src_tail = tail[team][src]

    if head[team][dst] == 0:

        head[team][dst] = src_head
        tail[team][dst] = src_tail


    else:
        next[tail[team][dst]] = src_head
        tail[team][dst] = src_tail

    head[team][src] = 0
    tail[team][src] = 0

def updateTeam(mTeam, mChangeScore):
    # 팀 전체의 평판 점수 변경
    # 변경 결과는 1~5 범위로 제한

    if mChangeScore == 0:
        return

    if mChangeScore > 0:
        scores = range(5, 0, -1)
    else:
        scores = range(1, 6)

    for score in scores:
        new_score = score + mChangeScore
        if new_score > 5:
            new_score = 5
        elif new_score < 1:
            new_score = 1

        move_group(mTeam, score, new_score)
        
def bestSoldier(mTeam):
    # 팀에서 평판 점수가 가장 높은 병사의 ID 반환
    # 동점이면 ID가 가장 큰 병사 선택
    for score in range(5, 0, -1):
        best_id = 0
        node = head[mTeam][score]

        while node != 0:
            mID = node_soldier[node]
            current = soldiers.get(mID)


            if current != None and current[1] == node:
                best_id = max(best_id, mID)

            node = next[node]

        if best_id > 0:
            return best_id

    return 0