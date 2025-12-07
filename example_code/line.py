from XRPLib.defaults import *
from lib import map
from lib import qwiic_huskylens

right = EncodedMotor.get_default_encoded_motor(2)

left = EncodedMotor.get_default_encoded_motor(1)

# this is a better line follow script, this one to use simply import this and use the command line.follow(90) in this case the target rpm is 90 which is quite fast but you can change it simply like this line.follow(30)
        
def follow(speed):
    # Create instance of device
    myHuskyLens = qwiic_huskylens.QwiicHuskyLens()
    objects = myHuskyLens.get_objects_of_interest()
    lines = myHuskyLens.get_lines_of_interest()
    
    # Check if it's connected
    if myHuskyLens.is_connected() == False:
        print("Device not connected, please check your connection",
            file=sys.stderr)
    

    # Initialize the device
    if myHuskyLens.begin() == False:
        print("Failed to initialize the device, please check your connection",
            file=sys.stderr)
            
    lines = myHuskyLens.get_lines_of_interest()
    for line in lines:
    
        if int(line.xTarget) < 160:
            error = map.map_range(int(line.xTarget), 0, 160, -speed, speed)
            left.set_speed(error)
            right.set_speed(speed)
        elif int(line.xTarget) > 160:
            error = map.map_range(int(line.xTarget), 0, 160, speed, -speed)
            left.set_speed(speed)
            right.set_speed(error)
        else:
            left.set_speed(speed)
            right.set_speed(speed)
    
