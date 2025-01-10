# 문제 번호: 2525
# 제목: 오븐 시계
a, b= map(int, input().split())
c = int(input())

if(b+c < 60) :
    print(a, b+c)
elif(b+c >= 60) :
    d = 0
    d = (b+c) // 60
    if((a+d) >= 24) :
        print((a+d) % 24, (b + c) % 60)
    else :
        print(a+d, (b+c) % 60)