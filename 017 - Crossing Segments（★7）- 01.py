# 017 - Crossing Segments（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_q
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/017-01.cpp

# Step #1. Input
N,M = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(M)]
L,R = [list(i) for i in zip(*_L)]

# Step #2. Brute Force
Answer = 0
for i in range(M):
    for j in range(i+1,M):
        if L[i] == L[j] or L[i] == R[j] or R[i] == L[j] or R[i] == R[j]:
            continue
        vec = []
        vec.append((L[i], 1))
        vec.append((R[i], 1))
        vec.append((L[j], 2))
        vec.append((R[j], 2))
        vec.sort()
        if vec[0][1] == 1 and vec[1][1] == 2 and vec[2][1] == 1 and vec[3][1] == 2:
            Answer += 1
        if vec[0][1] == 2 and vec[1][1] == 1 and vec[2][1] == 2 and vec[3][1] == 1:
            Answer += 1

# Step #3. Output The Answer!
print(Answer)