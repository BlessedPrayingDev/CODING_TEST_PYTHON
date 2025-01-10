# 문제 번호: 2884
# 제목: 알람 시계
H, M= map(int, input().split())

if(H <= 24 and M <= 59) :
    if (H >= 1 and M < 45):
        print("%d %d" % (H-1, M - 45 + 60))
    elif (H == 0 and M < 45):
        print("%d %d" % (H-1+24, M - 45 + 60))
    elif(M >= 45):
        print("%d %d" % (H, M - 45))