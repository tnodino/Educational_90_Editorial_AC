# 010 - Score Sum Queries（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_j
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/010.cpp

# Step #1. 入力
N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
C,P = [list(i) for i in zip(*_L)]
Q = int(input())
_L = [list(map(int,input().split())) for _ in range(Q)]
L,R = [list(i) for i in zip(*_L)]

# Step #2. 1 組・2 組それぞれの累積和を取る
Sum1 = [0] * (N+1)
Sum2 = [0] * (N+1)
for i in range(N):
    Sum1[i+1] = Sum1[i]
    Sum2[i+1] = Sum2[i]
    if C[i] == 1:
        Sum1[i+1] += P[i]
    if C[i] == 2:
        Sum2[i+1] += P[i]

# Step #3. クエリに答える
for i in range(Q):
    Answer1 = Sum1[R[i]] - Sum1[L[i]-1]
    Answer2 = Sum2[R[i]] - Sum2[L[i]-1]
    print(Answer1, Answer2)