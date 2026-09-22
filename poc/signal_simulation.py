import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

# 1. Generate time array (50ms duration)
t = np.linspace(0, 0.05, 5000)

# 2. Generate 18kHz-22kHz linear acoustic sweep
w = chirp(t, f0=18000, f1=22000, t1=0.05, method='linear')

# 3. Plot the signal (Simulating the "Emit" phase)
plt.plot(t, w)
plt.title('EchoScan Acoustic Sweep (18kHz - 22kHz)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
