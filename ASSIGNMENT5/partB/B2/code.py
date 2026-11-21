def decision(network, permission, sensitive, priority):
    if not permission and sensitive: return 'CANCEL'
    if network=='none': return 'DEFER'
    if network in ('wifi','cell'): return 'START'
    return 'DEFER'

for c in [('wifi',True,True,1),('none',True,True,1),('wifi',False,True,3)]:
    print(c,'->',decision(*c))
