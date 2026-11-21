from dataclasses import dataclass
@dataclass
class C:
    battery:int; charging:bool; net:str; moving:bool; saver:bool=False; temp:float=25

def policy(c):
    if c.temp>=42: return 300,'defer'
    if c.charging and c.net=='WIFI': return 10,'batch_now'
    if c.saver or c.battery<=15: return 300,'defer'
    if c.net=='NONE': return (30 if c.moving else 120),'defer'
    if c.battery<=30: return (60 if c.moving else 120),'defer'
    return (15 if c.moving else 60),('batch_now' if c.net=='WIFI' else 'batch_lte')

cases=[C(70,True,'WIFI',False),C(80,False,'LTE',True),C(20,False,'LTE',False),C(50,False,'LTE',True,True),C(60,False,'NONE',True),C(70,False,'WIFI',True,False,45),C(10,False,'LTE',True)]
for i,c in enumerate(cases,1): print(i,policy(c))
