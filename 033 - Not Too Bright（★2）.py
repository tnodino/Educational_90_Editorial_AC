# 033 - Not Too Bright（★2）
# https://atcoder.jp/contests/typical90/tasks/typical90_ag
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/033.cpp

H,W = map(int,input().split())
if H == 1 or W == 1:
    print(H * W)
else:
    print(((H + 1) // 2) * ((W + 1) // 2))