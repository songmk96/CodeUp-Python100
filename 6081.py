"""
16진수 입력을 몰랐을 때 : if-else 문으로 해결
"""
x = input()

if x == 'A':
    n = int(10)
elif x == 'B':
    n = int(11)
elif x == 'C':
    n = int(12)
elif x == 'D':
    n = int(13)
elif x == 'E':
    n = int(14)
else: n = int(15)

for i in range(1,16):
    print('%X'%n,'*%X'%i,'=%X'%(n*i),sep='')


"""
16진수 입력을 알았을 때 : int의 두 번째 인자에 원하는 진수를 적으면 됨
"""
n = int(input(), 16)

for i in range(1, 16) :
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')