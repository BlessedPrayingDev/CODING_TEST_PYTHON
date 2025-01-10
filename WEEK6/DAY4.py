# 문제 번호: 10952
# 제목: A+B -5
# 날짜: 25.01.10(금)
while True :
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        break
    print(A+B)

# 이런 방법도 있음
# import sys
# while True:
#     a,b=map(int,sys.stdin.readline().split())
#     if a==0 and b==0: break
#     print(a+b)