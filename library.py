from enum import Enum
import serial
import time

#byte 1 of the message is the numvber of the pair {0,1,2,3}
class FIU_PAIR(Enum):
    PAIR_1 = '1'
    PAIR_2 = '2'
    PAIR_3 = '3'
    PAIR_4 = '4'

#byte 2 of the message is the operation type (open-load or volatge injection)
class FIU_OPERATION(Enum):
    Open_Load = 'O'
    Volt_Injection = 'I'

#byte 3,4,5 of the message 
#when an open load opearion is chosen, there is two cases
class FIU_OL_MODE(Enum):
    OPEN_CIRCUIT = '100'
    CLOSED_CIRCUIT = '000'

#when a volatge injection is chosen, we should sepcify the voltage between 0V and 20.0V with a step of 0.1V
class FIU_VOLTAGE(Enum):
    VOLTAGE_00_0 = '000' # voltage = 00.0V
    VOLTAGE_01_3 = '013' # voltage = 01.3V
    VOLTAGE_01_4 = '014' # voltage = 01.4V
    VOLTAGE_01_5 = '015'
    VOLTAGE_01_6 = '016'
    VOLTAGE_01_7 = '017'
    VOLTAGE_01_8 = '018'
    VOLTAGE_01_9 = '019'
    VOLTAGE_02_0 = '020'
    VOLTAGE_02_1 = '021'
    VOLTAGE_02_2 = '022'
    VOLTAGE_02_3 = '023'
    VOLTAGE_02_4 = '024'
    VOLTAGE_02_5 = '025'
    VOLTAGE_02_6 = '026'
    VOLTAGE_02_7 = '027'
    VOLTAGE_02_8 = '028'
    VOLTAGE_02_9 = '029'
    VOLTAGE_03_0 = '030'
    VOLTAGE_03_1 = '031'
    VOLTAGE_03_2 = '032'
    VOLTAGE_03_3 = '033'
    VOLTAGE_03_4 = '034'
    VOLTAGE_03_5 = '035'
    VOLTAGE_03_6 = '036'
    VOLTAGE_03_7 = '037'
    VOLTAGE_03_8 = '038'
    VOLTAGE_03_9 = '039'
    VOLTAGE_04_0 = '040'
    VOLTAGE_04_1 = '041'
    VOLTAGE_04_2 = '042'
    VOLTAGE_04_3 = '043'
    VOLTAGE_04_4 = '044'
    VOLTAGE_04_5 = '045'
    VOLTAGE_04_6 = '046'
    VOLTAGE_04_7 = '047'
    VOLTAGE_04_8 = '048'
    VOLTAGE_04_9 = '049'
    VOLTAGE_05_0 = '050'
    VOLTAGE_05_1 = '051'
    VOLTAGE_05_2 = '052'
    VOLTAGE_05_3 = '053'
    VOLTAGE_05_4 = '054'
    VOLTAGE_05_5 = '055'
    VOLTAGE_05_6 = '056'
    VOLTAGE_05_7 = '057'
    VOLTAGE_05_8 = '058'
    VOLTAGE_05_9 = '059'
    VOLTAGE_06_0 = '060'
    VOLTAGE_06_1 = '061'
    VOLTAGE_06_2 = '062'
    VOLTAGE_06_3 = '063'
    VOLTAGE_06_4 = '064'
    VOLTAGE_06_5 = '065'
    VOLTAGE_06_6 = '066'
    VOLTAGE_06_7 = '067'
    VOLTAGE_06_8 = '068'
    VOLTAGE_06_9 = '069'
    VOLTAGE_07_0 = '070'
    VOLTAGE_07_1 = '071'
    VOLTAGE_07_2 = '072'
    VOLTAGE_07_3 = '073'
    VOLTAGE_07_4 = '074'
    VOLTAGE_07_5 = '075'
    VOLTAGE_07_6 = '076'
    VOLTAGE_07_7 = '077'
    VOLTAGE_07_8 = '078'
    VOLTAGE_07_9 = '079'
    VOLTAGE_08_0 = '080'
    VOLTAGE_08_1 = '081'
    VOLTAGE_08_2 = '082'
    VOLTAGE_08_3 = '083'
    VOLTAGE_08_4 = '084'
    VOLTAGE_08_5 = '085'
    VOLTAGE_08_6 = '086'
    VOLTAGE_08_7 = '087'
    VOLTAGE_08_8 = '088'
    VOLTAGE_08_9 = '089'
    VOLTAGE_09_0 = '090'
    VOLTAGE_09_1 = '091'
    VOLTAGE_09_2 = '092'
    VOLTAGE_09_3 = '093'
    VOLTAGE_09_4 = '094'
    VOLTAGE_09_5 = '095'
    VOLTAGE_09_6 = '096'
    VOLTAGE_09_7 = '097'
    VOLTAGE_09_8 = '098'
    VOLTAGE_09_9 = '099'
    VOLTAGE_10_0 = '100'
    VOLTAGE_10_1 = '101'
    VOLTAGE_10_2 = '102'
    VOLTAGE_10_3 = '103'
    VOLTAGE_10_4 = '104'
    VOLTAGE_10_5 = '105'
    VOLTAGE_10_6 = '106'
    VOLTAGE_10_7 = '107'
    VOLTAGE_10_8 = '108'
    VOLTAGE_10_9 = '109'
    VOLTAGE_11_0 = '110'
    VOLTAGE_11_1 = '111'
    VOLTAGE_11_2 = '112'
    VOLTAGE_11_3 = '113'
    VOLTAGE_11_4 = '114'
    VOLTAGE_11_5 = '115'
    VOLTAGE_11_6 = '116'
    VOLTAGE_11_7 = '117'
    VOLTAGE_11_8 = '118'
    VOLTAGE_11_9 = '119'
    VOLTAGE_12_0 = '120'
    VOLTAGE_12_1 = '121'
    VOLTAGE_12_2 = '122'
    VOLTAGE_12_3 = '123'
    VOLTAGE_12_4 = '124'
    VOLTAGE_12_5 = '125'
    VOLTAGE_12_6 = '126'
    VOLTAGE_12_7 = '127'
    VOLTAGE_12_8 = '128'
    VOLTAGE_12_9 = '129'
    VOLTAGE_13_0 = '130'
    VOLTAGE_13_1 = '131'
    VOLTAGE_13_2 = '132'
    VOLTAGE_13_3 = '133'
    VOLTAGE_13_4 = '134'
    VOLTAGE_13_5 = '135'
    VOLTAGE_13_6 = '136'
    VOLTAGE_13_7 = '137'
    VOLTAGE_13_8 = '138'
    VOLTAGE_13_9 = '139'
    VOLTAGE_14_0 = '140'
    VOLTAGE_14_1 = '141'
    VOLTAGE_14_2 = '142'
    VOLTAGE_14_3 = '143'
    VOLTAGE_14_4 = '144'
    VOLTAGE_14_5 = '145'
    VOLTAGE_14_6 = '146'
    VOLTAGE_14_7 = '147'
    VOLTAGE_14_8 = '148'
    VOLTAGE_14_9 = '149'
    VOLTAGE_15_0 = '150'
    VOLTAGE_15_1 = '151'
    VOLTAGE_15_2 = '152'
    VOLTAGE_15_3 = '153'
    VOLTAGE_15_4 = '154'
    VOLTAGE_15_5 = '155'
    VOLTAGE_15_6 = '156'
    VOLTAGE_15_7 = '157'
    VOLTAGE_15_8 = '158'
    VOLTAGE_15_9 = '159'
    VOLTAGE_16_0 = '160'
    VOLTAGE_16_1 = '161'
    VOLTAGE_16_2 = '162'
    VOLTAGE_16_3 = '163'
    VOLTAGE_16_4 = '164'
    VOLTAGE_16_5 = '165'
    VOLTAGE_16_6 = '166'
    VOLTAGE_16_7 = '167'
    VOLTAGE_16_8 = '168'
    VOLTAGE_16_9 = '169'
    VOLTAGE_17_0 = '170'
    VOLTAGE_17_1 = '171'
    VOLTAGE_17_2 = '172'
    VOLTAGE_17_3 = '173'
    VOLTAGE_17_4 = '174'
    VOLTAGE_17_5 = '175'
    VOLTAGE_17_6 = '176'
    VOLTAGE_17_7 = '177'
    VOLTAGE_17_8 = '178'
    VOLTAGE_17_9 = '179'
    VOLTAGE_18_0 = '180'
    VOLTAGE_18_1 = '181'
    VOLTAGE_18_2 = '182'
    VOLTAGE_18_3 = '183'
    VOLTAGE_18_4 = '184'
    VOLTAGE_18_5 = '185'
    VOLTAGE_18_6 = '186'
    VOLTAGE_18_7 = '187'
    VOLTAGE_18_8 = '188'
    VOLTAGE_18_9 = '189'
    VOLTAGE_19_0 = '190'
    VOLTAGE_19_1 = '191'
    VOLTAGE_19_2 = '192'
    VOLTAGE_19_3 = '193'
    VOLTAGE_19_4 = '194'
    VOLTAGE_19_5 = '195'
    VOLTAGE_19_6 = '196'
    VOLTAGE_19_7 = '197'
    VOLTAGE_19_8 = '198'
    VOLTAGE_19_9 = '199'
    VOLTAGE_20_0 = '200'


def calculate_checksum(message):
    checksum = 0
    for char in message:
        checksum ^= ord(char)
    return checksum

def FIU_construct_command(pair, operation, ol_mode=None, voltage=None):
    message = ""
    
    # Add byte 1 (pair)
    message += pair.value
    
    # Add byte 2 (operation)
    message += operation.value
    
    # Add bytes 3, 4, 5 based on the operation type
    if operation == FIU_OPERATION.Open_Load:
        if ol_mode is None:
            raise ValueError("opel_load mode value is required for opel_load operation")
        message += ol_mode.value
    elif operation == FIU_OPERATION.Volt_Injection:
        if voltage is None:
            raise ValueError("Voltage value is required for Volt_Injection operation")
        message += voltage.value
    
    #add checksum byte
    checksum= calculate_checksum(message)
    message= message + chr(checksum)

    return message



def FIU_start_successful_connection(com_port):
    # Configure the serial port
    serial_port = serial.Serial(com_port, 115200, timeout=1)

    message="CCCCCC"
    
    # Send the message
    serial_port.write(message.encode())

    start_time = time.time()  # Enregistrer le temps de départ
    while True:
        # Lire le message d'acquittement depuis le port série
        acknowledgment = serial_port.readline().decode().strip()
        if acknowledgment:
            break
        # Si aucun message n'est reçu après 2 secondes, sortir de la boucle
        if time.time() - start_time >= 2:
            print("Timeout: No acknowledgment received within 2 seconds")
            break

    # Check if acknowledgment is 'RD'
    if acknowledgment != 'RD':
        raise ConnectionError("Failed to establish connection.")
    else:
        print("Communication succeeded!")
    
    return serial_port

def FIU_close_serial_port(serial_port):
    serial_port.close()
    print("Serial port closed successfully.")


def FIU_execute_command(serial_port, message):
    # Send the message
    serial_port.write(message.encode())
    

    start_time = time.time()  # Enregistrer le temps de départ
    while True:
        # Lire le message d'acquittement depuis le port série
        acknowledgment = serial_port.read(2)
        if acknowledgment:
            break
        # Si aucun message n'est reçu après 2 secondes, sortir de la boucle
        if time.time() - start_time >= 2:
            print("Timeout: No acknowledgment received within 2 seconds")
            break
    
    # Check if acknowledgment is 'OK'
    if acknowledgment == b'OK':
        print("Command sent succuessfully!")
    elif acknowledgment == b'NK':
         raise ValueError("Resend the message, the message received by the MCU is corrupted!")
    else:
        raise ValueError("Failed to receive expected acknowledgment 'OK'.")

    
    return acknowledgment

