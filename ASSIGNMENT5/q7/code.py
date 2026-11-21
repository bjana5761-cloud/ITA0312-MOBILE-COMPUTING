"""Q7: Hybrid emergency communication network design."""
import matplotlib.pyplot as plt
l2=50; discovery=500; registration=150; total=l2+discovery+registration
print(f'Mobile IP handoff delay = {l2}+{discovery}+{registration} = {total} ms')
print('Architecture: responder AODV mesh -> redundant gateway/FA -> LTE/5G or satellite -> HA/AAA/VPN/control centre')
components=['L2','Discovery','Registration']; values=[l2,discovery,registration]
plt.figure(figsize=(7,4)); plt.bar(components,values); plt.ylabel('Delay (ms)'); plt.title('Q7: Mobile IP handoff delay budget'); plt.grid(axis='y',alpha=.3); plt.tight_layout(); plt.savefig('handoff_delay_budget.png',dpi=160)
