"""Q2: Mobile IPv4 registration, tunnelling and handoff-delay model."""
import matplotlib.pyplot as plt
home='130.10.5.20'; ha='130.10.5.1'; coa='192.168.40.1'; cn='200.50.60.7'
print('MN home:',home); print('Registration: MN -> FA/CoA -> HA'); print('Tunnel: CN -> HA -> CoA -> MN'); print('Basic Mobile IPv4 reply path: MN -> CN (triangular routing).')
advertisement_intervals=[0.5,1.0,1.5,2.0]; delay_ms=[50+500*t+150 for t in advertisement_intervals]
for t,d in zip(advertisement_intervals,delay_ms): print(f'Advertisement interval {t:.1f}s -> estimated handoff delay {d:.0f} ms')
plt.figure(figsize=(7,4)); plt.plot(advertisement_intervals,delay_ms,'o-'); plt.xlabel('Advertisement interval (s)'); plt.ylabel('Estimated handoff delay (ms)'); plt.title('Q2: Mobile IP handoff delay'); plt.grid(alpha=.3); plt.tight_layout(); plt.savefig('handoff_delay.png',dpi=160)
