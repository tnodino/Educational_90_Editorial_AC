# 002 - Encyclopedia of Parentheses（★3）
# https://atcoder.jp/contests/typical90/tasks/typical90_b
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/002.cpp

def hantei(S):
    dep = 0
    for i in range(len(S)):
        if S[i] == '(':
            dep += 1
        if S[i] == ')':
            dep -= 1
        if dep < 0:
            return False
    if dep == 0:
        return True
    return False

N = int(input())
for i in range(1<<N):
    Candidate = ''
    for j in range(N-1,-1,-1):
        # メモ : (i & (1 << j)) = 0 というのは、i の j ビット目（2^j の位）が 0 であるための条件。
        #       頻出なので知っておくようにしましょう。
        if i & (1 << j) == 0:
            Candidate += '('
        else:
            Candidate += ')'
    I = hantei(Candidate)
    if I == True:
        print(Candidate)