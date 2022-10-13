from BGen import BinaryGenerator
import numpy as np
import matplotlib.pyplot as plt

fm = 5
am = 1.0
Fs = 1000 * fm
t = np.arange(0, 1, 1/Fs)
msg_signal = am * np.sin(2 * np.pi * fm * t)
swt_signal = BinaryGenerator.generateSawtooth(t,fm*10,am)

op_signal = [1 if(msg_signal[i] >= swt_signal[i]) else 0 for i in range(len(t))]

plt.plot(t,op_signal)
plt.show()