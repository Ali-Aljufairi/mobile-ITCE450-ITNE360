# Singal power Free-space model 

import math
import numpy as np
import matplotlib.pyplot as plt

# Define the variables
d = np.arange(1, 10000, 1) # distance in meters
d0 = 1 # reference distance in meters
PtdBm = 0 # transmit power in dBm
Gt = 1 # transmit antenna gain in dBi
Gr = 1 # receive antenna gain in dBi
B = 1 # bandwidth in MHz
hT = 30 # transmit antenna height in meters
hR = 1.5 # receive antenna height in meters
c = 3*10**8 # speed of light in m/s
f = 2.4*10**9 # frequency in Hz
L = 4 # system loss in dB
Pt = 39  # transmit power in dBm 

