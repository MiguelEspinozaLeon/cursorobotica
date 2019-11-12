from pyfirmata import Arduino
import time

board = Arduino("COM3")
ledV = board.get_pin('d:9:o')
ledA = board.get_pin('d:8:o')
ledR = board.get_pin('d:10:o')
while True:
    ledV.write(1)
    time.sleep(3)
    ledV.write(0)
    ledA.write(1)
    time.sleep(3)
    ledA.write(0)
    ledR.write(1)
    time.sleep(3)
    ledR.write(0)
    


    