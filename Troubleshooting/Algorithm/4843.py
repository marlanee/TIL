# 특별한 정렬. 1차 시도: PASS(25분)

# 1. 목표: max, min, max -1, min + 1 순으로 정렬하여 10번째 숫자까지 출력하는 것
# 2. 구조: 빈 리스트를 만들고, 원래 리스트를 오람
    # 1. 빈 리스트를 만듦 / target_list = []
    # 2. 원래 리스트는 오름차순으로 정렬함 / sort(numbers)
    # 3. 뒤에서 하나, 앞에서 하나씩 꺼내서 빈 리스트에 더함. / numbers[N - 1 - i], numbers[i]
    # 4. 반복문의 범위는 N // 2
# 3. 종료: for 반복문이 (N // 2) + 1 에 도달하면 종료 후 target_list를 언패킹해서 10개까지 출력

# 아래는 sorted 함수를 사용한 풀이 코드

# T =int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     numbers = sorted(list(map(int, input().split())))   # 주어진 숫자들
#     target_list = []    # 특별한 정렬을 담는 리스트

#     for i in range(N // 2): # 뒤에서 하나(최댓값), 앞에서 하나(최솟값)씩을 빼서 target_list에 더함
#         target_list.append(numbers[N - 1 - i])  # 최댓값
#         target_list.append(numbers[i])  # 최솟값

#     print(f'#{tc}', end = ' ')
#     print(*target_list[:10])    # 언패킹하여 10개까지 출력

# 아래는 sorted 함수 없이 bubble_sort 사용한 코드

def bubble_sort(numbers, size):
    for i in range(size - 1, 0, -1):
        for j in range(i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

T =int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))   # 주어진 숫자들
    bubble_sort(numbers, N)
    target_list = []    # 특별한 정렬을 담는 리스트

    for i in range(N // 2): # 뒤에서 하나(최댓값), 앞에서 하나(최솟값)씩을 빼서 target_list에 더함
        target_list.append(numbers[N - 1 - i])  # 최댓값
        target_list.append(numbers[i])  # 최솟값

    print(f'#{tc}', end = ' ')
    print(*target_list[:10])    # 언패킹하여 10개까지 출력