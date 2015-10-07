import numpy as np
import matplotlib.pyplot as plt

Fs = 150.0
Ts = 1.0/Fs
t = np.arange(0,1,Ts)

ff = 5
y = np.sin(2*np.pi*ff+t)

n = len(y)
k = np.arange(n)
T = n/Fs
frq = k/T
frq=[range(n/2)]
Y = np.fft.fft(y)/n
Y = Y[range(n/2)]

fig, ax = plt.subplots(2, 1)

ax[0].plot(t,y)
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
#ax[1].plot(frq,abs(Y),'r') # plotting the spectrum
#ax[1].set_xlabel('Freq (Hz)')
#ax[1].set_ylabel('|Y(freq)|')


plt.show()