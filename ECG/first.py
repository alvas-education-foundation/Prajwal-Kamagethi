import numpy as np
from biosppy.signals import ecg

# load raw ECG signal
signal = np.loadtxt('a01_3.csv')

# process it and plot
out = ecg.ecg(signal=signal, sampling_rate=1000., show=True)
