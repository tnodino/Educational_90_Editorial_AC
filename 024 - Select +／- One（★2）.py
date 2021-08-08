# 024 - Select +／- One（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_x
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/024.cpp

# Step #1. Input
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# Step #2. Check Difference
Diff = 0
for i in range(N):
    Diff += abs(A[i] - B[i])
if Diff > K:
    print('No')
    exit()

# Step #3. Check Parity
if Diff % 2 != K % 2:
    print('No')
    exit()

# Step #4. Output Yes
print('Yes')