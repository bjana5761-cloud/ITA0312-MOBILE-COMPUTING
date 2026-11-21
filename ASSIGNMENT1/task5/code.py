# Task 5
subscribers=[1000,10000,20000,100000]
sites={"S1":[5,13,25,125],"S2a":[5,9,17,85],"S2b":[5,6,11,51]}
for s,counts in sites.items():
    print(s, list(zip(subscribers,counts)))
