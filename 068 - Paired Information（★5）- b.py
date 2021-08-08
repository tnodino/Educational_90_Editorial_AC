# 068 - Paired Information（★5）
# https://atcoder.jp/contests/typical90/tasks/typical90_bp
# https://github.com/E869120/kyopro_educational_90/blob/main/sol/068b.cpp

class segtree():
    n=1
    size=1
    log=2
    d=[0]
    op=None
    e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V)
        self.op=OP
        self.e=E
        self.log=(self.n-1).bit_length()
        self.size=1<<self.log
        self.d=[E for i in range(2*self.size)]
        for i in range(self.n):
            self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):
            self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size
        self.d[p]=x
        for i in range(1,self.log+1):
            self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e
        smr=self.e
        l+=self.size
        r+=self.size
        while(l<r):
            if (l&1):
                sml=self.op(sml,self.d[l])
                l+=1
            if (r&1):
                smr=self.op(self.d[r-1],smr)
                r-=1
            l>>=1
            r>>=1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:
            return self.n
        l+=self.size
        sm=self.e
        while(1):
            while(l%2==0):
                l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):
                        sm=self.op(sm,self.d[l])
                        l+=1
                return l-self.size
            sm=self.op(sm,self.d[l])
            l+=1
            if (l&-l)==l:
                break
        return self.n
    def min_left(self,r,f):
        assert 0<=r and r<self.n
        assert f(self.e)
        if r==0:
            return 0
        r+=self.size
        sm=self.e
        while(1):
            r-=1
            while(r>1 & (r%2)):
                r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):
                        sm=self.op(self.d[r],sm)
                        r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:
                break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])

def _add(x, y):
    return x + y

N = int(input())
Q = int(input())
_L = [list(map(int,input().split())) for _ in range(Q)]
T,X,Y,V = [list(i) for i in zip(*_L)]
_sum = [0] * N
for i in range(Q):
    if T[i] == 0:
        _sum[X[i]] = V[i]
pot = [0] * (N+1)
for i in range(1,N):
    pot[i+1] = _sum[i] - pot[i]
s = segtree([1] * N, _add, 0)
for i in range(Q):
    if T[i] == 0:
        s.set(X[i], 0)
    else:
        p = min(X[i], Y[i])
        q = max(X[i], Y[i])
        it = s.prod(p, q)
        if it == 0:
            print(pot[Y[i]] + (V[i] - pot[X[i]]) if (q - p) % 2 == 0 else pot[Y[i]] - (V[i] - pot[X[i]]))
        else:
            print('Ambiguous')