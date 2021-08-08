# 014 - We Used to Sing a Song Together（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_n
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/014.cpp

# Step #1. 入力
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# Step #2. ソート
A.sort()
B.sort()

# Step #3. 出力
Answer = 0
for i in range(N):
    Answer += abs(A[i] - B[i])
print(Answer)