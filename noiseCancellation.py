def butter_lowpass(cutoff, fs, order=5):
nyq = 0.5 * fs
normal_cutoff = cutoff / nyq
b, a = butter(order, normal_cutoff, btype=’low’, analog=False)
return b, a
def butter_lowpass_filter(data, cutoff, fs, order=5):
b, a = butter_lowpass(cutoff, fs, order=order)
y = lfilter(b, a, data)
return y
# remez (fir) design arguements
Fpass = 10e6 # passband edge
Fstop = 11.1e6 # stopband edge, transition band 100kHz
Wp = Fpass/(Fs) # pass normalized frequency
Ws = Fstop/(Fs) # stop normalized frequency
# iirdesign agruements
Wip = (Fpass)/(Fs/2)
Wis = (Fstop+1e6)/(Fs/2)
Rp = 1 # passband ripple
As = 42 # stopband attenuation
