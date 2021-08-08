# 016 - Minimum Coins（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_p
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/016.cpp

N = int(input())
A,B,C = map(int,input().split())
Answer = 1<<30
for i in range(9999):
    for j in range(9999):
        V = N - i * A - j * B
        R = i + j + V // C
        if V % C != 0 or V < 0 or R > 9999:
            continue
        Answer = min(Answer, R)
print(Answer)