import serial
import time

port = 'COM7'

arduino = serial.Serial(port,9600,timeout = 0.1)

#gives command and then gives another command later
time.sleep(10)
arduino.write("A")

time.sleep(3)
arduino.write("B")
arduino.write("D")
arduino.write("A")


x = 0 
while(x<1000):
    print(arduino.readline())
    x=x+1
    





arduino.write("B")

arduino.close()
