"""
3,6,9 조건문을 각각 if-else문으로 나눠준 경우
"""
n = int(input())

for i in range(1, n+1):
    if i%10 == 3:
        print("X", end=' ')
    elif i%10 == 6:
        print("X", end=' ')
    elif i%10 == 9:
        print("X", end=' ')
    else:
        print(i, end=' ')

"""
3,6,9 조건문을 or로 합쳐준 경우
"""
n = int(input())

for i in range(1, n+1) :
  if i%10 == 3 or i%10 == 6 or i%10 == 9 :
    print("X", end=' ')
  else :
    print(i, end=' ')