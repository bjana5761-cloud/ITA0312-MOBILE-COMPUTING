import math

def spatial_reuse_gain(angle_deg, beamwidth=20):
    return max(0.0, angle_deg/beamwidth)

for a in (5,10,20,30,45,60):
    print(f'Angular separation {a:2d}° -> relative spatial separation {spatial_reuse_gain(a):.2f}')
print('SDMA decision: reuse the same channel only when angular separation is sufficient for the required SIR.')
