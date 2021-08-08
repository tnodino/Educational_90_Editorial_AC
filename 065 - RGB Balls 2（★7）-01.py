# 065 - RGB Balls 2（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_bm
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/065-01.cpp

# Step #1. 入力・前処理
R,G,B,K = map(int,input().split())
X,Y,Z = map(int,input().split())
assert(R + G + B <= 15)

# Step #2. bit 全探索
Answer = 0
for i in range(1<<(R+G+B)):
    cntr = 0
    cntg = 0
    cntb = 0
    for j in range(R+G+B):
        if i & (1 << j) == 0:
            continue
        if j < R:
            cntr += 1
        elif j < R + G:
            cntg += 1
        else:
            cntb += 1
    if cntr + cntg <= X and cntg + cntb <= Y and cntb + cntr <= Z and cntr + cntg + cntb == K:
        Answer += 1

# Srep #3. 出力
print(Answer)