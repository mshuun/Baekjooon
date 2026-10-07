def solution(n):
    answer = []
    digits = "124"

    while n > 0:
        n -= 1
        answer.append(digits[n % 3])
        n //= 3

    return ''.join(reversed(answer))