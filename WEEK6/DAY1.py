# 문제 번호: 11022
# 제목: A+B -8
T = int(input())
for i in range(T) :
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(i+1, A, B, A+B))