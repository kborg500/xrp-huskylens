import qwiic_i2c
import sys

# Provide all required arguments: id, scl pin, and sda pin
i2c = qwiic_i2c.get_i2c_driver(id=0, scl=5, sda=4) 

if i2c is None:
    print("Failed to connect to I2C bus. Check pins/ID.")
else:
    print("I2C bus connected. Scanning...")
    devices = i2c.scan()
    print("I2C devices found:", devices)
