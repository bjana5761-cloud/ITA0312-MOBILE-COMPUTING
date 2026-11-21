scores={
'D1 Cellular voice':('FDMA',3.90),
'D2 Tactical link':('CDMA',3.60),
'D3 Stadium downlink':('OFDMA',4.10),
'D4 5,000 sensors':('OFDMA',3.45)}
for d,(t,s) in scores.items(): print(f'{d}: {t} ({s:.2f}/5)')
