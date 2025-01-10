# 문제 번호: 15552
# 제목: 빠른 A+B
import sys

T = int(input())

for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
