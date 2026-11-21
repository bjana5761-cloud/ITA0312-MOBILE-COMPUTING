RES={'360p':1.0,'480p':1.8,'720p':4.0,'1080p':9.0}
BR={'360p':[500,800,1200],'480p':[900,1400,2000],'720p':[1800,2800,4000],'1080p':[3500,5500,8000]}

def choose(cpu,battery,net,mbps,charging=False):
    if battery<15 and not charging: timing='wait_charge'
    elif net!='wifi' and mbps<5: timing='wait_wifi'
    else: timing='now'
    chosen=None
    for r,f in RES.items():
        enc=15*f*.25/cpu
        if enc<=12: chosen=r
    if chosen is None: chosen='360p'
    limits=.06 if battery<30 else .12
    bitrate=BR[chosen][0]
    for b in BR[chosen]:
        size=b*15/8000
        bw=20 if timing=='wait_wifi' else max(mbps,0.1)
        up=size*8/bw
        impact=0 if timing=='wait_charge' else 0.01*up
        if up<=20 and impact<=limits: bitrate=b
    return chosen,bitrate,timing

samples=[('D1',3,85,'wifi',40),('D2',3,60,'5g',35),('D3',2.2,15,'4g',8),('D4',1.2,55,'4g',12),('D5',1.0,25,'4g',3),('D6',0.8,10,'4g',8),('D7',2.5,70,'wifi',20),('D8',1.5,45,'5g',2)]
for d,cpu,bat,net,bw in samples: print(d,choose(cpu,bat,net,bw))
