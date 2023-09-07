def pascalTriangle(h):
    res = []    # 결과값 저장 리스트
    pre = []    # 이전 높이에 해당하는 리스트
    pre.append(1)
    res.append(pre)
    for i in range(1, h):
        cur = []    # 현재 높이에 저장할 값 저장(초기화)
        cur.append(1)  
        j = 0
        while (j < len(pre) - 1):
            cur.append(pre[j] + pre[j+1])
            j += 1
        cur.append(1)
        res.append(cur)
        pre = cur
    return res

H = int(input('높이 입력 : '))
result = pascalTriangle(H)
for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()
