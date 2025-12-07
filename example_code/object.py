from XRPLib.defaults import *
from lib import map
from lib import qwiic_huskylens
import time

#this is code that checks the center position of an object being track and then moves accordengly, i used map wich is built into arduino but doseint come built into micropython, to use this youll have to create a python script in the lib folder with the code of this:
#import time
#
#def map_range(value, in_min, in_max, out_min, out_max):
#
#    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min



right = EncodedMotor.get_default_encoded_motor(2)

left = EncodedMotor.get_default_encoded_motor(1)

kp = 1
        
def track(speed):
    # Create instance of device
    myHuskyLens = qwiic_huskylens.QwiicHuskyLens()
    objects = myHuskyLens.get_objects_of_interest()
    
    # Check if it's connected
    if myHuskyLens.is_connected() == False:
        print("Device not connected, please check your connection",
            file=sys.stderr)
    

    # Initialize the device
    if myHuskyLens.begin() == False:
        print("Failed to initialize the device, please check your connection",
            file=sys.stderr)
    #print("tracking")
    for object in objects:
        
        
        error = map.map_range(int(object.xCenter), 0, 320, -speed, speed)
        left.set_speed(error)
        right.set_speed(-error)
       
    
while __name__ == '__main__':
    track(90)

       
        