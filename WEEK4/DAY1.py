H, M= map(int, input().split())

if(H <= 24 and M <= 59) :
    if (H >= 1 and M < 45):
        H = H - 1
        print("%d %d" % (H, M - 45 + 60))
    elif (H == 0 and M < 45):
        H = H - 1 + 24
        print("%d %d" % (H, M - 45 + 60))
    elif(M >= 45):
        print("%d %d" % (H, M - 45))