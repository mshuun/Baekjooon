def closest_bathroom(N, mascot, K):
    # 화장실 유형 결정: 안뇽이(용)는 홀수 층, 인덕이(오리)는 짝수 층
    if mascot == "annyong":  # 안뇽이(용)의 경우
        if K % 2 == 1:  # 이미 홀수 층에 있다면
            return K
        else:  # 가장 가까운 홀수 층 찾기
            return K - 1 if K - 1 > 0 else K + 1

    elif mascot == "induck":  # 인덕이(오리)의 경우
        if K % 2 == 0:  # 이미 짝수 층에 있다면
            return K
        else:  # 가장 가까운 짝수 층 찾기
            return K + 1 if K + 1 <= N else K - 1

# 예제 입력 1
print(closest_bathroom(int(input()), input(), int(input())))  # 예상 출력: 3 또는 5

