import smbus2
import struct
import time

SLAVE_ADDR = 0x0A # I2C Address of Arduino 1

# Name of the file in which the log is kept
LOG_FILE = './temp.log'

# Initialize the I2C bus;
# RPI version 1 requires smbus.SMBus(0)
i2c = smbus2.SMBus(1)

def readTemperature():
    try:
        msg = smbus2.i2c_msg.read(SLAVE_ADDR, 4)
        i2c.i2c_rdwr(msg)
        data = list(msg)
        dataStr = ''.join([chr(c) for c in data])
        dataBytes = bytes(dataStr, encoding="raw_unicode_escape")

        temp = struct.unpack('<f'
                             , dataBytes)
        print('Received temp: {0} = {1:.2f}'.format(data, temp[0]))
        return temp[0]
    except Exception as e:
        print("Error reading")
        print(e)
        return None
def log_temp(temperature):
    try:
        with open(LOG_FILE, 'a+') as fp:
            fp.write('Date:{0} Temp:{1:.2f}C\n'.format(time.asctime(time.localtime(time.time())),temperature))
    except Exception as e:
        print(e)
        return
def main():
    while True:
        try:
            cTemp = readTemperature()
            log_temp(cTemp)
            time.sleep(1)
        except KeyboardInterrupt:
            return
if __name__ == '__main__':
    main()