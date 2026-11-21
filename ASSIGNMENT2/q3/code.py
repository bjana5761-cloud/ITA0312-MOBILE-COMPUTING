import math

def processing_gain(L): return 10*math.log10(L)

for L in (8,16,64):
    print(f'L={L}: processing gain={processing_gain(L):.2f} dB')
print('Near-far example, L=64, K=8: BER 0.009 at equal power, 0.037 at +10 dB, 0.259 at +20 dB.')
print('Power control is required so users arrive near the target Eb/I0.')
