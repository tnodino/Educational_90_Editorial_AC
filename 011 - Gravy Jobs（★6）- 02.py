# 011 - Gravy Jobs（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_k
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/011-01.cpp

def hantei(mask):
    CurrentTime = 0
    CurrentMoney = 0
    for i in range(N):
        if mask & (1 << i) == 0:
            continue
        if CurrentTime + C[i] > D[i]:
            return -1
        else:
            CurrentTime += C[i]
            CurrentMoney += S[i]
    return CurrentMoney

# Step #1. 入力
# Step #2. D[i] の昇順にソート
N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
_L.sort()
D,C,S = [list(i) for i in zip(*_L)]

# Step #3. やる仕事を bit 全探索
Answer = 0
for i in range(1<<N):
    Score = hantei(i)
    Answer = max(Answer, Score)

# Step #4. 出力
print(Answer)