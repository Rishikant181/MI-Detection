import scipy.io.wavfile as wavfile
import numpy as np

# Load the .wav file
sample_rate, audio_data = wavfile.read('./samples/raw/test_signal4.wav')

# Scale the normalized audio samples to the voltage range
voltage_values = audio_data

# Export the voltage values to a text file
np.savetxt('./samples/converted/test_signal4.txt', voltage_values)
