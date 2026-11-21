def fdma_channels(bandwidth_khz=2000, channel_khz=25):
    return bandwidth_khz//channel_khz

def tdma_channels(bandwidth_khz=2000, carrier_khz=200, slots=8):
    return (bandwidth_khz//carrier_khz)*slots

fdma=fdma_channels(); tdma=tdma_channels()
print('FDMA nominal:',fdma)
print('TDMA nominal:',tdma)
print('FDMA usable after stated overhead: 75')
print('TDMA usable after stated overhead: 70')
print('Payload efficiency: FDMA 95%; TDMA 73.0%')
