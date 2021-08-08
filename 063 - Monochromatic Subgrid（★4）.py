# 063 - Monochromatic Subgrid（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_bk
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/063.cpp

from collections import defaultdict

def maximum_same(R):
    Map = defaultdict(int)
    ret = 0
    for i in range(len(R)):
        Map[R[i]] += 1
        ret = max(ret, Map[R[i]])
    return ret

# Step #1. 入力
H,W = map(int,input().split())
P = [list(map(int,input().split())) for _ in range(H)]

# Step #2. 答えを求める
Answer = 0
for i in range(1,1<<H):
    R = []
    for j in range(W):
        idx = -1
        flag = False
        for k in range(H):
            if i & (1 << k) == 0:
                continue
            if idx == -1:
                idx = P[k][j]
            elif idx != P[k][j]:
                flag = True
        if flag == False:
            R.append(idx)
    cntH = 0
    cntW = maximum_same(R)
    for j in range(H):
        if i & (1 << j) != 0:
            cntH += 1
    Answer = max(Answer, cntH * cntW)
print(Answer)