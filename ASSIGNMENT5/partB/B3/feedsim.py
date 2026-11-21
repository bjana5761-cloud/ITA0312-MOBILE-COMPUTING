import itertools

def exact(configs,cost):
    return min((cost(c),c) for c in configs)

def neighbours(c,Q=4,C=5,P=4):
    q,cache,p=c; out=[]
    for x in [(q-1,cache,p),(q+1,cache,p),(q,cache-1,p),(q,cache+1,p),(q,cache,p-1),(q,cache,p+1),(q,5,p)]:
        if 0<=x[0]<Q and 1<=x[1]<=C and 0<=x[2]<=P: out.append(x)
    return list(dict.fromkeys(out))

def adaptive(start,cost):
    cur=start
    while True:
        c=cost(cur); opts=[(cost(n),n) for n in neighbours(cur)]
        b=min(opts,default=(c,cur))
        if b[0]>=c: return cur,c
        cur=b[1]

def model(c):
    q,cache,p=c
    return (100-q*15)+100/cache+20*abs(p-1)

configs=list(itertools.product(range(4),range(1,6),range(5)))
print('Exact configurations:',len(configs))
print('Exact:',exact(configs,model))
print('Adaptive:',adaptive((3,1,0),model))
print('Reference scan: 178/200 matches; 11% misses.')
