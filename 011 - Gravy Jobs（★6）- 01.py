# 011 - Gravy Jobs（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_k
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/011-01.cpp

from itertools import permutations

# Step #1. 入力
N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
D,C,S = [list(i) for i in zip(*_L)]

# Step #2. 順列全探索
Answer = 0
for ord in permutations([i for i in range(N)],N):
    CurrentTime = 0
    CurrentMoney = 0
    for i in range(N):
        if CurrentTime + C[ord[i]] <= D[ord[i]]:
            CurrentTime += C[ord[i]]
            CurrentMoney += S[ord[i]]
        else:
            break
    Answer = max(Answer, CurrentMoney)

# Step #3. 出力
print(Answer)