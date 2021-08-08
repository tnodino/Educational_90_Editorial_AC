# 051 - Typical Shop（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_ay
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/051.cpp

from bisect import bisect_left

# Step #1. 入力
N,K,P = map(int,input().split())
A = list(map(int,input().split()))

# Step #2. 半分全列挙
mid = N // 2
vec1 = [[] for _ in range(N+1)]
vec2 = [[] for _ in range(N+1)]
for i in range(1<<mid):
    cnt1 = 0
    cnt2 = 0
    for j in range(mid):
        if i & (1 << j) != 0:
            cnt1 += A[j]
            cnt2 += 1
    vec1[cnt2].append(cnt1)
for i in range(1<<(N-mid)):
    cnt1 = 0
    cnt2 = 0
    for j in range(N-mid):
        if i & (1 << j) != 0:
            cnt1 += A[mid+j]
            cnt2 += 1
    vec2[cnt2].append(cnt1)

# Step #3. 答えを求める
for i in range(N+1):
    vec1[i].sort()
    vec2[i].sort()
Answer = 0
for h in range(K+1):
    for i in range(len(vec1[h])):
        pos1 = bisect_left(vec2[K-h], P - vec1[h][i] + 1)
        Answer += pos1

# Step #4. 出力
print(Answer)