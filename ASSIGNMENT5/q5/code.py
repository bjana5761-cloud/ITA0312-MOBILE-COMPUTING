"""Q5: DSDV proactive-routing analysis using the assignment's reported values."""
import matplotlib.pyplot as plt
nodes=[10,20,30,40,50]; overhead=[3.6,8.7,19.3,37.5,66.2]; pdr=[39.7,76.5,89.2,93.7,93.0]
for n,o,p in zip(nodes,overhead,pdr): print(f'N={n}: overhead={o} msgs/delivered packet, PDR={p}%')
fig,ax1=plt.subplots(figsize=(7,4)); ax1.plot(nodes,overhead,'o-',label='Control overhead'); ax1.set_xlabel('Number of nodes'); ax1.set_ylabel('Control msgs / delivered packet'); ax1.grid(alpha=.3); ax2=ax1.twinx(); ax2.plot(nodes,pdr,'s--',label='PDR'); ax2.set_ylabel('Packet delivery ratio (%)'); ax2.set_ylim(0,105); plt.title('Q5: DSDV overhead and delivery vs network size'); fig.tight_layout(); fig.savefig('dsdv_scaling.png',dpi=160)
speed=[0,2,5,10,20]; speed_overhead=[27.8,43.0,66.2,110.0,212.0]
plt.figure(figsize=(7,4)); plt.plot(speed,speed_overhead,'o-'); plt.xlabel('Speed (m/s)'); plt.ylabel('Control msgs / delivered packet'); plt.title('Q5: DSDV overhead vs mobility'); plt.grid(alpha=.3); plt.tight_layout(); plt.savefig('dsdv_mobility.png',dpi=160)
