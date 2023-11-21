k, a, b = map(int, input().split())

def max_chocolates(k, a, b):
    # 계산을 위해 a와 b를 k로 나누어줍니다. 
    # a를 k로 나누었을 때 나머지를 빼서 k의 배수가 되도록 조정합니다.
    if a % k != 0:
        a = a + (k - a % k)
    
    # b를 k로 나누었을 때 나머지를 더해서 k의 배수가 되도록 조정합니다.
    if b % k != 0:
        b = b - (b % k)

    # k의 배수의 개수를 계산합니다.
    # 예외 처리: a > b 인 경우는 초콜릿이 없으므로 0을 반환합니다.
    if a > b:
        return 0
    else:
        return (b - a) // k + 1
print(max_chocolates(k,a,b))