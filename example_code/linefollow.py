
# x locaton str(object.xCenter)
# y location str(object.yCenter)
# object with str(object.width)
# object hight str(object.height)

# line id, zero = unknown str(line.id))
# line x start str(line.xOrigin)
# line x end str(line.xTarget)
# line y start str(line.yOrigin)
# line y end str(line.yTarget)

from XRPLib.defaults import *
from lib import qwiic_huskylens 
import sys
import time
from XRPLib.board import Board
from XRPLib.encoded_motor import EncodedMotor
# this is code ment to follow a line useing the husky lens camera, make sure there is a good contrast and any texture in the background can be missred as a line
motor2 = EncodedMotor.get_default_encoded_motor(2)

motor1 = EncodedMotor.get_default_encoded_motor(1)

board = Board.get_default_board()

effort = 40

board = Board.get_default_board()

def linefollow():
    print("\nhusky line followinggg\n")

    # Create instance of device
    myHuskyLens = qwiic_huskylens.QwiicHuskyLens()

    # Check if it's connected
    if myHuskyLens.is_connected() == False:
        print("Device not connected, please check your connection",
            file=sys.stderr)
        return

    # Initialize the device
    if myHuskyLens.begin() == False:
        print("Failed to initialize the device, please check your connection",
            file=sys.stderr)
        return

    board.wait_for_button()

    nScans = 0
    while True:
   
        objects = myHuskyLens.get_objects_of_interest()
        lines = myHuskyLens.get_lines_of_interest()
        
        if len(lines) == 0:
            print("Nothing found, point HuskyLens at something it recognizes")
            motor1.set_speed(0)
            motor2.set_speed(0)
            continue

        
        
        #when lines repete this code
        for line in lines:
            og_error = line.xOrigin - 160
            future_error = line.xTarget - line.xOrigin
            print(future_error)
            

            motor1.set_speed(future_error + effort)
            motor2.set_speed(effort)
            
            
            if future_error == 0:
                motor1.set_speed(30)
                motor2.set_speed(30)
        
            

if __name__ == '__main__':
    try:
        linefollow()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example")
        sys.exit(0)

