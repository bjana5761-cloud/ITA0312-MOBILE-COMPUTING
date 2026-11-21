def feasible(item, env):
    if not env['permission']: return False
    if item['sensitive'] and not item['encrypted']: return False
    if env['network']=='none': return False
    if env['battery'] < 20 and item['priority'] < 3: return False
    if env['doze'] and item['priority'] < 3: return False
    return True

items=[{'id':'R1','priority':2,'sensitive':True,'encrypted':True}, {'id':'R2','priority':1,'sensitive':True,'encrypted':True}, {'id':'R3','priority':1,'sensitive':True,'encrypted':True}, {'id':'A1','priority':3,'sensitive':True,'encrypted':True}]
env={'permission':True,'network':'cell','battery':57.6,'doze':False}
for x in items: print(x['id'], 'FEASIBLE' if feasible(x,env) else 'DEFER')
