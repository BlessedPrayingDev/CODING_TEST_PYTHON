# 문제 번호: 10430
# 제목: 나머지
a, b, c = map(int, input().split());
print((a+b)%c)
print(((a%c) + (b%c))%c)
print((a*b)%c)
print(((a%c) * (b%c))%c)