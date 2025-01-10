# 문제 번호: 2439
# 제목: 별 찍기 -2
N = int(input())

for i in range(1, N + 1) :
    print("%s%s"%((" " * 3),("*"*i)))