# 문제 번호: 14681
# 제목: 사분면 고르기
x = int(input())
y = int(input())
if(x > 0 and y > 0) :
    print(1)
elif(x < 0 and y > 0) :
    print(2)
elif(x < 0 and y < 0) :
    print(3)
elif(x > 0 and y < 0) :
    print(4)