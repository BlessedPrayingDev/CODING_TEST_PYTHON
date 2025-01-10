# 문제 번호: 25304
# 제목: 영수증
totAmt = int(input())
itemCount = int(input())
sum = 0
for i in range(itemCount) :
    a, b= map(int, input().split())
    sum += (a * b)
print("Yes" if totAmt == sum else "No")