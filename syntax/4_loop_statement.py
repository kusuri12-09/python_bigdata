# 0부터 4까지 5번 반복하며 i값 출력
for i in range(5):
   print('iteration', i)

print('\n')

# 1부터 9까지 5번 반복 (홀수번)
for i in range(1, 10, 2):
   print('iteration', i)

# for 문
sum = 0
for i in range(1, 11):
   sum = sum + i
print('합계=', sum)

#while 문
i = 1
sum = 0
while i < 11:
   sum = sum + i
   i = i + 1
print('합계=', sum)

# 주어진 숫자만큼 문자를 반복
def rept(string, n):
   n_st=''
   for i in range(n):
     n_st = n_st + string
   print(n_st)

string = input('문자를 입력하고 Enter: ')
n = int(input('정수숫자를 입력하고 Enter: '))

rept(string, n)