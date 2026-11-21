"""Q4: Mobile IP application suitability scoring."""
import matplotlib.pyplot as plt
scores={'Session continuity':5,'Delay':4,'Interruption':4,'Overhead':4,'Security':4,'Scalability':4}
print(f'Average suitability score: {sum(scores.values())/len(scores):.2f}/5')
for k,v in scores.items(): print(f'{k}: {v}/5')
plt.figure(figsize=(8,4)); plt.bar(scores.keys(),scores.values()); plt.ylim(0,5.5); plt.ylabel('Score / 5'); plt.xticks(rotation=25,ha='right'); plt.title('Q4: Mobile IP application suitability'); plt.grid(axis='y',alpha=.3); plt.tight_layout(); plt.savefig('mobile_ip_suitability.png',dpi=160)
