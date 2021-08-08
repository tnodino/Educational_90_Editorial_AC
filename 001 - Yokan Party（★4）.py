# 001 - Yokan Party（★4）
# https://atcoder.jp/contests/typical90/tasks/typical90_a
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/001.cpp

def solve(m):
    cnt = 0
    pre = 0
    for i in range(N):
        if A[i] - pre >= m and L - A[i] >= m:
            cnt += 1
            pre = A[i]
    if cnt >= K:
        return True
    return False

# Step #1. 入力
N,L = map(int,input().split())
K = int(input())
A = list(map(int,input().split()))

# Step #2. 答えで二分探索（めぐる式二分探索法）
# https://qiita.com/drken/items/97e37dd6143e33a64c8c
left = -1
right = L + 1
while right - left > 1:
    mid = left + (right - left) // 2
    if solve(mid) == False:
        right = mid
    else:
        left = mid
print(left)