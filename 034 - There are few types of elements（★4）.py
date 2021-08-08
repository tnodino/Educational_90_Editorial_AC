# 034 - There are few types of elements（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_ah
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/034.cpp

from collections import defaultdict

# Step #1. Input
N,K = map(int,input().split())
A = list(map(int,input().split()))

# Step #2. Shakutori
cr = 0
cnt = 0
Map = defaultdict(int)
Answer = 0
for i in range(N):
    while cr < N:
        if Map[A[cr]] == 0 and cnt == K:
            break
        if Map[A[cr]] == 0:
            cnt += 1
        Map[A[cr]] += 1
        cr += 1
    Answer = max(Answer, cr - i)
    if Map[A[i]] == 1:
        cnt -= 1
    Map[A[i]] -= 1

# Step #3. Output The Answer
print(Answer)