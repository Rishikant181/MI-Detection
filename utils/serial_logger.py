from serial import Serial
import numpy
from scipy.io import wavfile

def serial_to_wave(filename, fs):
    '''
    Logs the given data to a file.

    Args:
        - filename (string): The name of the wave file to which data is to be written.
        - fs (int): The sampling frequency of the wave file.
    '''
    # Initializing serial connection to COM3
    serial = Serial('com3')

    # Stores the recorded signal's samples
    signal = numpy.array([])

    try:
        while True:
            # Getting current intensity
            intensity = int(serial.readline().decode('utf-8').strip('\n'))
        
            # Appending to output array
            signal = numpy.append(signal, intensity)

    except KeyboardInterrupt:
        # Writing to wave file
        wavfile.write(filename, fs, signal)

serial_to_wave('test_signal.wav', 500)