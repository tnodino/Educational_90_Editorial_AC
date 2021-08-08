# 064 - Uplift（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_bl
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/064.cpp

# Step #1. 入力
N,Q = map(int,input().split())
A = list(map(int,input().split()))
L,R,V = [],[],[]
for _ in range(Q):
    l,r,v = map(int,input().split())
    l -= 1
    r -= 1
    L.append(l)
    R.append(r)
    V.append(v)

# Step #2. 最初の答え
B = [0] * N
Answer = 0
for i in range(N-1):
    B[i] = A[i+1] - A[i]
    Answer += abs(B[i])

# Step #3. シミュレーション
for i in range(Q):
    mae = abs(B[L[i] - 1]) + abs(B[R[i]])
    if L[i] > 0:
        B[L[i] - 1] += V[i]
    if R[i] < N - 1:
        B[R[i]] -= V[i]
    ato = abs(B[L[i] - 1]) + abs(B[R[i]])
    Answer += (ato - mae)
    print(Answer)