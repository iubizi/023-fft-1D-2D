import numpy as np

# The period is 2pi, and according to the Nyquist sampling law (2x),
# the minimum sampling frequency is pi.
# The engineering sampling rate is more than 5 times.
signal = np.sin(np.arange(10*np.pi, step=0.1*np.pi))
print('len(signal) =', len(signal))

import matplotlib.pyplot as plt
plt.plot(signal)
plt.title('signal')
plt.show()

fft = np.fft.fft(signal)
print('len(fft) =', len(fft))

# Amplitude spectrum
# symmetrical two peaks
plt.plot(abs(fft))
plt.title('fft')
plt.show()
