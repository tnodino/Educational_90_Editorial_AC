# 089 - Partitions and Inversions（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_ck
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/089-01.cpp

mod = 10**9+7

N,K = map(int,input().split())
A = list(map(int,input().split()))
Answer = 1
for i in range(N-1):
    if A[i] <= A[i+1]:
        Answer *= 2
        Answer %= mod
print(Answer)