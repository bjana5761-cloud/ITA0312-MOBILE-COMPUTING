states={'S0 ACTIVE':'screen on; normal scheduling','S1 IDLE':'screen off; limited CPU activity','S2 SUSPENDED':'CPU suspended; kernel wake sources only','S3 MAINTENANCE':'brief wake for deferred jobs/sync'}
for s,d in states.items(): print(s,'->',d)
print('Reference energy / 30 min: wake-lock 36 mAh; compliant 8.4 mAh; deep batching 4.1 mAh; conflicting 41 mAh')
