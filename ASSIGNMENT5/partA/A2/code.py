def sync_incremental(records, network, battery, budget):
    sent=[]; deferred=[]; spent=0
    records=sorted([r for r in records if r['dirty']], key=lambda r:(-r['priority'],r['size']))
    for r in records:
        if network=='none' or battery<20 and r['priority']<3:
            deferred.append(r['id']); continue
        if spent+r['size']>budget:
            deferred.append(r['id']); continue
        if r['sensitive'] and not r['encrypted']:
            deferred.append(r['id']); continue
        sent.append(r['id']); spent+=r['size']
    return sent,deferred

records=[{'id':'r1','dirty':True,'priority':3,'size':20,'sensitive':True,'encrypted':True},{'id':'r2','dirty':True,'priority':1,'size':150,'sensitive':True,'encrypted':True}]
print(sync_incremental(records,'wifi',70,120))
