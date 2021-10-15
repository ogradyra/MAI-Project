import numpy as np 
import math
import matplotlib.pyplot as plt

length = 10
sr = 48000.0
f1 = 2

waveform = [math.sin((2.0*math.pi*f1*i/sr) - (2*math.pi)) for i in range(int(length*sr))]
timeBins = [i/sr for i in range(len(waveform))]

spectrum = np.fft.rfft(waveform)
spectrumMod = 20.0 * np.log10(np.abs(spectrum))
spectrumPha  = 180.0 / np.pi * np.angle(spectrum)
freqBins = [i/len(spectrum) * sr / 2.0 for i in range(len(spectrum))]

# 180.0 / np.pi * 

# waveform plot
plt.plot(timeBins, waveform, '-')
plt.title('Sine Wave')
plt.xlim([0, 20*(1/f1)]) # plot for 10ns or 20 periods
plt.xlabel('Time [ns]')
plt.ylabel('Amplitude')
plt.grid(1)
#plt.show()

# spectrum plot

# magnitude plot
plt.subplot(2,1,1)
plt.title('Spectrum of a sine wave')
plt.semilogx(freqBins, spectrumMod, label='Sine Wave Magnitude')
plt.grid(1)
plt.legend(loc='upper left')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power [dB]')

# phase plot
plt.subplot(2,1,2)
plt.semilogx(freqBins, spectrumPha, label='Sine Wave Phase')
plt.grid(1)
plt.legend(loc='upper left')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Phase [Degrees]')
plt.show()


