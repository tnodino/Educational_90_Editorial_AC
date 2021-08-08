# 066 - Various Arrays（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bn
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/066b.cpp

def calc(la, ra, lb, rb):
    ra += 1
    rb += 1
    sep = [la, ra, lb, rb]
    sep.sort()
    all = 0
    cnt = 0
    for i in range(3):
        for j in range(3):
            if la <= sep[i] and sep[i+1] <= ra and lb <= sep[j] and sep[j+1] <= rb:
                all += (sep[i+1] - sep[i]) * (sep[j+1] - sep[j])
                if i > j:
                    cnt += (sep[i+1] - sep[i]) * (sep[j+1] - sep[j])
                elif i == j:
                    cnt += (sep[i+1] - sep[i]) * (sep[i+1] - sep[i] - 1) // 2
    return cnt / all

N = int(input())
L,R = [],[]
for _ in range(N):
    l,r = map(int,input().split())
    L.append(l)
    R.append(r)
expsum = 0.0
for i in range(N):
    for j in range(i+1,N):
        expsum += calc(L[i], R[i], L[j], R[j])
print(expsum)