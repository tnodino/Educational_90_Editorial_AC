# 066 - Various Arrays（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bn
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/066a.cpp

N = int(input())
_L = [list(map(int,input().split())) for _ in range(N)]
L,R = [list(i) for i in zip(*_L)]
expsum = 0.0
for i in range(N):
    for j in range(i+1,N):
        cnt = 0
        all = 0
        for k in range(L[i],R[i]+1):
            for l in range(L[j],R[j]+1):
                if k > l:
                    cnt += 1
                all += 1
        expsum += cnt / all
print(expsum)