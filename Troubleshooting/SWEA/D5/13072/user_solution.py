soldiers = {}

def init():
    # 테스트 케이스 초기화
    soldiers.clear()
    return


def hire(mID, mTeam, mScore):
    # 병사 고용
    soldiers[mID] = (mTeam, mScore)


def fire(mID):
    # 병사 해고
    soldiers.pop(mID)


def updateSoldier(mID, mScore):
    # 병사 한 명의 평판 점수 변경
    team, score = soldiers[mID]
    soldiers[mID] = (team, mScore)


def updateTeam(mTeam, mChangeScore):
    # 팀 전체의 평판 점수 변경
    # 변경 결과는 1~5 범위로 제한
    for mID, (team, score) in soldiers.items():
        if team == mTeam:
            score = score + mChangeScore
            if score > 5:
                score = 5
            elif score < 1:
                score = 1
            soldiers[mID] = (team, score)


def bestSoldier(mTeam):
    # 팀에서 평판 점수가 가장 높은 병사의 ID 반환
    # 동점이면 ID가 가장 큰 병사 선택
    best_score = 0
    best_id = 0

    for mID, (team, score) in soldiers.items():
        if team != mTeam:
            continue

        if score > best_score:
            best_score = score
            best_id = mID
        elif score == best_score:
            best_id = max(best_id, mID)

    return best_id