# 031 - VS AtCoder（★6）
# https://atcoder.jp/contests/typical90/tasks/typical90_ae
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/031.cpp

def init():
    for i in range(51):
        for j in range(1501):
            mex = [0] * 1600
            if i >= 1:
                mex[grundy[i-1][j+i]] = 1
            if j >= 2:
                for k in range(1,j//2+1):
                    mex[grundy[i][j-k]] = 1
            for k in range(1600):
                if mex[k] == 0:
                    grundy[i][j] = k
                    break

# Step #1. Input
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# Step #2. Initialize
grundy = [[0] * 1600 for _ in range(51)]
init()

# Step #3. Get Answer
sum_xor = 0
for i in range(N):
    sum_xor ^= grundy[A[i]][B[i]]

# Step #4. Output
if sum_xor != 0:
    print('First')
if sum_xor == 0:
    print('Second')