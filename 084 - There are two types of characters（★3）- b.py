# 084 - There are two types of characters（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_cf
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/084-02.cpp

N = int(input())
S = input()
A = [0] * (N+1)
B = [0] * (N+1)
for i in range(1,N+1):
    if S[i-1] == 'o':
        A[i] = i
        B[i] = B[i-1]
    if S[i-1] == 'x':
        A[i] = A[i-1]
        B[i] = i
Answer = 0
for i in range(1,N+1):
    Answer += min(A[i], B[i])
print(Answer)