scores={'Session continuity':5,'Delay':4,'Interruption':4,'Overhead':4,'Security':4,'Scalability':4}
print('Mobile IP suitability score:',sum(scores.values())/len(scores),'/5')
for k,v in scores.items(): print(k,v,'/5')
