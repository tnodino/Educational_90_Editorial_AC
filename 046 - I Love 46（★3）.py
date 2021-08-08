# 046 - I Love 46（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_at
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/046.cpp

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
am = [0] * 46
bm = [0] * 46
cm = [0] * 46
for i in range(N):
    am[A[i] % 46] += 1
    bm[B[i] % 46] += 1
    cm[C[i] % 46] += 1
ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += am[i] * bm[j] * cm[k]
print(ans)