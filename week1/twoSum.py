def twoSum(a, n ,t):
    for i in range(n) :
        for j in range(i+1, n):
            if a[i] + a[j] == t :
                print(i + 1, '번째와 ', j + 1, '번째 원소\n')

import random
N = int(input('리스트의 원소 개수 : '))
A = []
for i in range(N):
    A.append(random.randint(1, N*2))
print('리스트 : ', A)
T = int(input('목표값 입력 : '))
print('두 수의 합이 %d인 원소 쌍'%T)
twoSum(A, N, T)