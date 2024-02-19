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

    # Stores the recorded signals' samples
    signals = numpy.array([])

    try:
        while True:
            # Getting current intensity
            intensity_str = int(serial.readline().decode('utf-8').strip('\n'))

            # Converting intensity string to a list of intensities from different channels
            intensities = [int(intensity) for intensity in intensity_str]
        
            # Appending to output array
            signals = numpy.append(signal, intensities, axis=0)

    except KeyboardInterrupt:
        # Writing to wave file(s)
        i = 0
        for signal in signals:
            wavfile.write(filename + i + ".wave", fs, signal)
            i += 1

serial_to_wave('test_signal', 500)