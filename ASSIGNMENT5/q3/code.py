"""Q3: Compare cellular and ad hoc wireless networks."""
import matplotlib.pyplot as plt
features=['Infrastructure','Central control','Multi-hop','Self-healing','Fast deployment']; cellular=[1,1,0,0,0]; ad_hoc=[0,0,1,1,1]
print('CELLULAR: infrastructure, base-station/core control and single-hop access')
print('AD HOC: distributed multi-hop routing, self-healing and no fixed tower required')
x=range(len(features)); w=.38
plt.figure(figsize=(8,4)); plt.bar([i-w/2 for i in x],cellular,width=w,label='Cellular'); plt.bar([i+w/2 for i in x],ad_hoc,width=w,label='Ad hoc')
plt.xticks(list(x),features,rotation=20,ha='right'); plt.yticks([0,1],['No','Yes']); plt.title('Q3: Cellular vs Ad Hoc features'); plt.legend(); plt.tight_layout(); plt.savefig('cellular_vs_adhoc.png',dpi=160)
