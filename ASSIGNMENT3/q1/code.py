"""Q1: Wireless architecture and mobility analysis. Calculates packet loss during handoff and generates an RSS plot."""
import numpy as np
import matplotlib.pyplot as plt
packet_rate=50
interruptions=[0.1,0.2,0.3,0.5]
print('Potential packets lost during handoff')
for t in interruptions: print(f'{t:.1f} s interruption -> {packet_rate*t:.0f} packets')
x=np.linspace(0,100,300); old=-45-0.45*x; new=-90+0.45*x
handoff=x[np.argmin(np.abs(old-new))]
plt.figure(figsize=(7,4)); plt.plot(x,old,label='Old AP RSSI'); plt.plot(x,new,label='New AP RSSI'); plt.axvline(handoff,ls='--',label='Handoff point')
plt.xlabel('User movement (%)'); plt.ylabel('RSSI (dBm)'); plt.title('Q1: RSSI-based handoff'); plt.grid(alpha=.3); plt.legend(); plt.tight_layout(); plt.savefig('handoff_rssi.png',dpi=160)
print(f'Estimated handoff point: {handoff:.1f}% of movement')
