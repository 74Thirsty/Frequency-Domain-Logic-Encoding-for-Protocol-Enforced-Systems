import numpy as np

import matplotlib.pyplot as plt
from scipy.signal import chirp, spectrogram

# Sampling rate
fs = 100_000
T = 1.0

# Generate a chirp from 1 kHz to 16 kHz over 1 s
t = np.linspace(0, T, int(fs*T), endpoint=False)
sig = chirp(t, f0=1_000, f1=16_000, t1=T, method='linear')

# 1) Zoomed waveform (first 5 ms)
zoom_T = 0.005
N_zoom = int(fs*zoom_T)
tz = t[:N_zoom]
sz = sig[:N_zoom]

plt.figure(figsize=(8, 3), dpi=200)
plt.plot(tz*1000.0, sz)
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.title('Chirp Waveform (First 5 ms)')
plt.tight_layout()
plt.savefig('waveform_zoom.png')
plt.close()

# 2) Multi-tone packet: 4 tones, 50 ms each
symbol_duration = 0.05
symbols = [1_000, 10_000, 16_000, 4_000]
packet = []

for f0 in symbols:
    t_sym = np.linspace(0, symbol_duration, int(fs*symbol_duration), endpoint=False)
    s_sym = np.sin(2*np.pi*f0*t_sym)
    packet.append(s_sym)

packet = np.concatenate(packet)

f2, tt2, Sxx2 = spectrogram(packet, fs=fs, nperseg=2048, noverlap=1024,
                            scaling='density', mode='magnitude')

plt.figure(figsize=(8, 4.5), dpi=200)
plt.pcolormesh(tt2, f2/1000.0, Sxx2, shading='gouraud')
plt.ylabel('Frequency [kHz]')
plt.xlabel('Time [s]')
plt.title('Multi-tone Symbol Packet (Discrete Logic States)')
plt.tight_layout()
plt.savefig('multitone_packet.png')
plt.close()

print("Generated: waveform_zoom.png, multitone_packet.png")

