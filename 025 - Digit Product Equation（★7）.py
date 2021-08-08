# 025 - Digit Product Equation（★7）
# https://atcoder.jp/contests/typical90/tasks/typical90_y
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/025.cpp

def dfs(pos, last, _str):
    global Answer
    if pos == 0:
        rem = 1
        for i in range(len(_str)):
            rem *= ord(_str[i]) - 48
        goal = rem + B
        if goal <= N:
            goal_str = list(str(goal))
            goal_str.sort()
            goal_str.reverse()
            goal_str = ''.join(goal_str)
            if goal_str == _str:
                Answer += 1
        return
    for i in range(last,0,-1):
        str2 = _str
        str2 += chr(i+48)
        dfs(pos - 1, i, str2)

Answer = 0
N,B = map(int,input().split())
for i in range(1,12):
    dfs(i, 9, '')
V = str(B)
flag = False
for i in range(len(V)):
    if V[i] == '0':
        flag = True
if flag == True and N >= B:
    Answer += 1
print(Answer)