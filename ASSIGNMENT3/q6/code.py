"""Q6: AODV reactive routing and DSDV comparison."""
import matplotlib.pyplot as plt
cases=['20/2','30/5','50/10','50/20','40/0']; dsdv_over=[7.0,19.3,110.0,212.0,17.8]; aodv_over=[3.1,3.1,7.5,12.8,0.15]
dsdv_pdr=[77.2,89.2,87.2,76.8,100.0]; aodv_pdr=[77.4,89.6,88.1,81.0,100.0]
for c,d,a in zip(cases,dsdv_over,aodv_over): print(f'N/speed={c}: DSDV={d}, AODV={a} control msgs/delivered packet')
x=range(len(cases)); w=.38
plt.figure(figsize=(8,4)); plt.bar([i-w/2 for i in x],dsdv_over,w,label='DSDV'); plt.bar([i+w/2 for i in x],aodv_over,w,label='AODV'); plt.xticks(list(x),cases); plt.ylabel('Control msgs / delivered packet'); plt.title('Q6: Routing overhead comparison'); plt.legend(); plt.tight_layout(); plt.savefig('aodv_dsdv_overhead.png',dpi=160)
plt.figure(figsize=(8,4)); plt.plot(cases,dsdv_pdr,'o-',label='DSDV PDR'); plt.plot(cases,aodv_pdr,'s--',label='AODV PDR'); plt.ylabel('Packet delivery ratio (%)'); plt.xlabel('Nodes / speed (m/s)'); plt.title('Q6: Packet delivery ratio comparison'); plt.grid(alpha=.3); plt.legend(); plt.tight_layout(); plt.savefig('aodv_dsdv_pdr.png',dpi=160)
