# 10. 23.
# Programmers 표 편집
# 1차 시도: FAIL(90분)
# 10. 26. 복습 필요

"""
목표: 명령어 cmd가 주어진다. 
    1. cmd에 따라 가상의 문자열 내에서 특정 index를 선택하거나, 삭제하거나, 복구한다
    2. 모든 cmd 명령을 수행한 후, 원본 문자열과 비교하여 삭제된 행은 X, 삭제되지 않은 행은 O로 표기하라
상태: 
자료구조:
핵심로직:
    1. cmd를 순회함 / while c < len(cmd): 
    2. cmd의 명령어에 따라 next 리스트를 수정함 / Z가 나오면 prev로 뒤집어 씌움
    3. cmd의 순회가 끝나면 원본과 비교하며 OX 문자열을 작성함 / set로 next를 형변환 -> range(n) 순회하며 문자열 붙이기
종료조건:
시간복잡도:
"""
def solution(n, k, cmd):
    c = 0
    prev = [i for i in range(-1, n - 1)]
    next = [i for i in range(1, n + 1)]
    next[-1] = -1
    deleted = []
    
    while  c < len(cmd):
        current = cmd[c].split()
        key = current[0]
        
        if key == 'U':
            for _ in range(int(current[1])):
                k = prev[k]
                
        elif  key == 'D':
            for _ in range(int(current[1])):
                k = next[k]
        
        elif key == 'C':
            left = prev[k]
            right = next[k]
            
            if right != -1:
                prev[right] = left
            if left != -1:
                next[left] = right
            
            deleted.append(k)
            
            if right != -1:
                k = right
            else:
                k = left
                
        elif key == 'Z':
            target = deleted.pop()
            left = prev[target]
            right = next[target]
            
            if right != -1:
                prev[right] = target
            
            if left != -1:
                next[left] = target
        
        c += 1
    
    answer = ['O'] * n
    
    for idx in deleted:
        answer[idx] = 'X'
        
    return ''.join(answer)