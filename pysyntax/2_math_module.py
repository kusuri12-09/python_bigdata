import math

# 근의공식 구하기
# a가 0이 아니고 2개의 해가 있다고 가정
a = int(input('a값을 입력하고 Enter: '))
b = int(input('b값을 입력하고 Enter: '))
c = int(input('c값을 입력하고 Enter: '))

d = b**2 - 4 * a * c

if d < 0:
    print("실근이 존재하지 않습니다. (허근)")
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)

    print('x1 =', x1)
    print('x2 =', x2)