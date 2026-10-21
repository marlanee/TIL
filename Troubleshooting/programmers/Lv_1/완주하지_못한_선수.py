def solution(participant, completion):
    part_dict = {}
    comp_dict = {}
    
    for p in participant:
        part_dict.setdefault(p, 0)
        part_dict[p] += 1
    
    for c in completion:
        comp_dict.setdefault(c, 0)
        comp_dict[c] += 1
        
    for part in part_dict:
        if part not in comp_dict:
            answer = part
            break
        if part_dict[part] != comp_dict[part]:
            answer = part
            break
            
    return answer