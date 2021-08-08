# 030 - K Factors（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_ad
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/030.cpp

# Step #1. Input
N,K = map(int,input().split())

# Step #2. Count Number
cnt = [0] * (N+1)
for i in range(2,N+1):
    if cnt[i] >= 1:
        continue
    for j in range(i,N+1,i):
        cnt[j] += 1

# Step #3. Get Answer
Answer = 0
for i in range(1,N+1):
    if cnt[i] >= K:
        Answer += 1
print(Answer)