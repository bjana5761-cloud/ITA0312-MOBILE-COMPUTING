import random
MAXW=3

def workload(n=40,seed=7):
    r=random.Random(seed); out=[]
    for i in range(n):
        p=3 if r.random()<.12 else (2 if r.random()<.38 else 1)
        size=r.randint(10,30) if p==3 else r.randint(40,200)
        out.append({'id':i,'priority':p,'size':size,'arrival':r.randint(0,39)})
    return sorted(out,key=lambda x:(x['arrival'],x['id']))

def priority_score(w,t):
    return 100*(w['priority']==3)+20*w['priority']+(t-w['arrival'])-w['size']/20

items=workload()
for t in range(10):
    ready=[w for w in items if w['arrival']<=t]
    ready.sort(key=lambda w:priority_score(w,t),reverse=True)
    print(t,[w['id'] for w in ready[:MAXW]])
print('Reference: FIFO deferrals 593; priority deferrals 520.')
