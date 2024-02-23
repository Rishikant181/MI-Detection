from serial import Serial
import numpy

def serial_to_wave(filename, fs):
    '''
    Logs the given data to a file.

    Args:
        - filename (string): The name of the wave file to which data is to be written.
        - fs (int): The sampling frequency of the wave file.
    '''
    # Calculating sampling delay
    delay = 1 / fs

    # Initializing serial connection to COM3
    serial = Serial('com3')

    # Stores the recorded signals' samples
    signals = numpy.zeros([1, 7])

    # Stores the current timestamp
    timestamp = 0

    try:
        while True:
            # Getting current intensity
            intensity_str = serial.readline().decode('utf-8').strip('\n').strip('\r')

            # Converting intensity string to a list of intensities from different channels
            intensities = numpy.array([[int(intensity) for intensity in intensity_str.split(',')]]) / 1000
        
            # Appending timestamp
            intensities = numpy.append([[timestamp]], intensities, axis=1)
            
            # Incremeting timestamp
            timestamp += delay
            
            # Appending to output array
            signals = numpy.append(signals, intensities, axis=0)

    except KeyboardInterrupt:
        # Writing to csv
        numpy.savetxt(filename, signals, delimiter=',')

serial_to_wave('test_signal.csv', 500)