def eratos(a, n):
	a[1] = 0
	for i in range (2, n//2 + 1):
		if a[i] != 0 :
			j = 2
			while i*j<=n :
				a[i*j] = 0
				j+=1
	return a

N = int(input('N = '))
while N < 1:
	print(N, '은(는) 자연수가 아닙니다.')
	N = int(input('N = '))
A = list(range(N+1))
res = eratos(A, N)
for i in range(N+1):
	if res[i]: print(i, end=' ')