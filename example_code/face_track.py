from mystuff.husky import object
from XRPLib.encoded_motor import EncodedMotor
from XRPLib.board import Board
import time

motor1 = EncodedMotor.get_default_encoded_motor(1)

board = Board.get_default_board()

# this is simple code ment to use the object example code to track faces automaticaly 



while True:
    if board.is_button_pressed() == 1:
        motor1.set_speed(0)
        motor1.set_speed(0)
        time.sleep(1)
    
    else:
        object.track(90)