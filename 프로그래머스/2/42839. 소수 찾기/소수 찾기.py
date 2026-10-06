from itertools import permutations as per
import math

def is_prime(n):
  if n <= 1:
    return False

  for i in range(2, int(math.isqrt(n)) + 1):
    if n % i == 0:
      return False

  return True

def solution(numbers):
    aa = []
    for i in range(1, len(numbers) + 1):
        aa = aa + [int(''.join(p)) for p in per(numbers, i)]
    aa = list(set(aa))
    c = 0
    for i in aa:
        if is_prime(i):
            c+=1
    return c
