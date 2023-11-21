def min_operations(A, B):
    from collections import deque

    queue = deque([(B, 0)])  # (현재 값, 연산 횟수)
    while queue:
        current, steps = queue.popleft()

        if current == A:
            return steps + 1  # 연산 횟수에 1을 더해서 반환
        if current < A:
            continue

        # 2로 나누는 연산
        if current % 2 == 0:
            queue.append((current // 2, steps + 1))

        # 오른쪽에 1을 제거하는 연산
        if str(current).endswith("1"):
            queue.append((int(str(current)[:-1]), steps + 1))

    return -1  # 변환할 수 없는 경우
a,b = map(int,input().split())
print(min_operations(a,b))
