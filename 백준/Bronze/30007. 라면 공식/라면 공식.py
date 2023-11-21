# 라면 끓이는 횟수 N 입력
N = int(input())

# 결과를 저장할 리스트 생성
result = []

# N번 반복하면서 라면 끓이기
for i in range(N):
    # 각 라면의 A, B, X 값 입력
    A, B, X = map(int, input().split())
    
    # 라면 공식에 따라 필요한 물의 양 W 계산
    W = A * (X - 1) + B
    
    # 결과 리스트에 추가
    result.append(W)

# 결과 출력
for W in result:
    print(W)
