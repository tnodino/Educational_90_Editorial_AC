# 017 - Crossing Segments（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_q
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/017-02.cpp

# Step #1. Input
N,M = map(int,input().split())
_L = [list(map(int,input().split())) for _ in range(M)]
L,R = [list(i) for i in zip(*_L)]

# Step #2. Get Answer1
V3 = [0] * (N+1)
Answer1 = 0
for i in range(M):
    V3[L[i]] += 1
    V3[R[i]] += 1
for i in range(N+1):
    Answer1 += V3[i] * (V3[i] - 1) // 2

# Step #3. Get Answer2
V1 = [0] * (N+1)
V2 = [0] * (N+1)
Answer2 = 0
for i in range(M):
    V1[R[i]] += 1
    V2[L[i]-1] += 1
for i in range(N):
    V1[i+1] += V1[i]
    Answer2 += V1[i+1] * V2[i+1]

# Step #4. Sorting
vec = []
for i in range(M):
    vec.append((R[i], L[i]))
vec.sort()

# Step #5. Get Answer3
cnt = [0] * (N+1)
Answer3 = 0
for i in range(len(vec)):
    cl = vec[i][1]
    cr = vec[i][0]
    ret = 0
    for j in range(cl+1,cr+1):
        ret += cnt[j]
    Answer3 += ret
    cnt[cl] += 1

# Step #6. Output The Answer!
Total = M * (M - 1) // 2
SumAns = Answer1 + Answer2 + Answer3
print(Total - SumAns)