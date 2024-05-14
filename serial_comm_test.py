import time
from library import FIU_close_serial_port, FIU_execute_command, FIU_start_successful_connection, FIU_construct_command, FIU_OL_MODE, FIU_PAIR, FIU_OPERATION, FIU_VOLTAGE
import serial


'''
# Configure the serial port
serial_port = serial.Serial('COM12', 9600, timeout=1)

# Wait for the serial port to initialize
time.sleep(2)

# Define the message to send
message = "1I190"

# Send the message
serial_port.write(message.encode())

# Close the serial port
serial_port.close()
'''

# Exemple d'utilisation :
if __name__ == "__main__":
    com_port = 'COM12'
    serial_port = FIU_start_successful_connection(com_port)
    command = FIU_construct_command(FIU_PAIR.PAIR_4, FIU_OPERATION.Volt_Injection,voltage=FIU_VOLTAGE.VOLTAGE_08_4)
    acknowledgment = FIU_execute_command(serial_port, command)
    print("Acknowledgment received:", acknowledgment)
    FIU_close_serial_port(serial_port)
