def bubbleSort(a, n):
   for i in range(n, 0, -1):
        for j in range(1, i):
            if a[j] > a[j+1]:
                a[j+1], a[j] = a[j], a[j+1]

def checkSort(a, n):
    isSorted = True

    for i in range(1, n):
        if a[i] > a[i+1]:
            isSorted = False
            
        if not isSorted:
            break

    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

import random, time

NN = [10000, 20000, 30000]
sortType = {None : "랜덤", True: "평순", False: "역순"}

for sort in sortType:
    for N in NN:
        a = []
        a.append(-1)
        for i in range(N):
            a.append(random.randint(1, N))

        if sort != None:
            a.sort(reverse=(not sort))

        start_time = time.time()

        bubbleSort(a, N) 

        end_time = time.time() - start_time
        print("정렬: %s"%(sortType[sort]))
        print("정렬의 실행 시간 (N=%d) : %0.3f"%(N, end_time))

        checkSort(a, N)
