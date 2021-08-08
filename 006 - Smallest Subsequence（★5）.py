# 006 - Smallest Subsequence（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_f
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/006.cpp

# Step #1. 入力
N,K = map(int,input().split())
S = input()

# Step #2. 前計算
nex = [[len(S)] * 26 for _ in range(len(S)+1)]
for i in range(len(S)-1,-1,-1):
    for j in range(26):
        if ord(S[i]) - 97 == j:
            nex[i][j] = i
        else:
            nex[i][j] = nex[i+1][j]

# Step #3. 一文字ずつ貪欲に決める
Answer = ''
CurrentPos = 0
for i in range(K):
    for j in range(26):
        NexPos = nex[CurrentPos][j]
        MaxPossibleLength = len(S) - NexPos + i
        if MaxPossibleLength >= K:
            Answer += chr(j + 97)
            CurrentPos = NexPos + 1
            break

# Step #4. 出力
print(Answer)