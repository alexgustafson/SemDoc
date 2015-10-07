'''
This code is adapted from the following URL:
https://plot.ly/matplotlib/fft/
'''

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

Fs = 441000.0
Ts = 1.0/Fs

ff = 5000;  # frequency of the signal

t = np.arange(0,1,Ts)
y = signal.sawtooth(2 * np.pi * ff * t)
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(n/2)]

fig, ax = plt.subplots(2, 2)

ax[0,0].plot(t[0:200], y[0:200])
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('Amplitude')
ax[1,0].plot(frq, abs(Y), 'r') # plotting the spectrum
ax[1,0].set_xlabel('Freq (Hz)')
ax[1,0].set_ylabel('|Y(freq)|')

Fs = 44100.0
Ts = 1.0/Fs

ff = 5000;  # frequency of the signal

t = np.arange(0,1,Ts)
y = signal.sawtooth(2 * np.pi * ff * t)
n = len(y) # length of the signal
k = np.arange(n)
T = n/Fs
frq = k/T # two sides frequency range
frq = frq[range(n/2)] # one side frequency range

Y = np.fft.fft(y)/n # fft computing and normalization
Y = Y[range(n/2)]

ax[0,1].plot(t[0:20], y[0:20])
ax[0,1].set_xlabel('Time')
ax[0,1].set_ylabel('Amplitude')
ax[1,1].plot(frq, abs(Y), 'r') # plotting the spectrum
ax[1,1].set_xlabel('Freq (Hz)')
ax[1,1s].set_ylabel('|Y(freq)|')

plt.show()