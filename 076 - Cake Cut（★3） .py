# 076 - Cake Cut（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_bx
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/076.cpp

from bisect import bisect_left

# Step #1. Input
N = int(input())
A = list(map(int,input().split()))

# Step #2. Make Array B
B = [0] * (2*N+1)
for i in range(N):
    B[i+1] = B[i] + A[i]
for i in range(N):
    B[i+N+1] = B[i+N] + A[i]
if B[N] % 10 != 0:
    print('No')
    exit()

# Step #3. Get Answer
for i in range(N+1):
    goal = B[i] + B[N] // 10
    pos1 = bisect_left(B, goal)
    if B[pos1] == goal:
        print('Yes')
        exit()
print('No')