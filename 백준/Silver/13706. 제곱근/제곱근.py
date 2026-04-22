def binary_search_sqrt(n):
    # 이진 탐색으로 제곱근을 찾는 함수
    # n: 찾고자 하는 정수

    left = 1  # 탐색 범위의 시작을 1로 설정
    right = n  # 탐색 범위의 끝을 n으로 설정

    while left <= right:
        mid = (left + right) // 2  # 중간 값을 계산하여 정수로 만듦
        square = mid * mid  # 중간 값의 제곱을 구함

        if square == n:
            # 중간 값의 제곱이 n과 같으면
            return mid  # 중간 값인 제곱근을 반환

        elif square < n:
            # 중간 값의 제곱이 n보다 작으면
            left = mid + 1  # 탐색 범위를 오른쪽으로 좁힘

        else:
            # 중간 값의 제곱이 n보다 크면
            right = mid - 1  # 탐색 범위를 왼쪽으로 좁힘


n = int(input())

result = binary_search_sqrt(n) 

print(result)
