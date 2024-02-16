from serial import Serial

def log(filename):
    '''
    Logs the given data to a file.

    Args:
        - data (string): The data to be logged
    '''
    # Initializing serial connection to COM3
    serial = Serial('com3')

    # Initializing file
    file = open(filename, 'w')

    for i in range(10):
        # Reading the current line from serial
        data = serial.readline().decode('utf-8').strip('\n')

        # Writing the line
        file.write(data)

    file.close()

log('test_data.csv')