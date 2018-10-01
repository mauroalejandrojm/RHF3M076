import serial
import time

ser = serial.Serial(
    port='/dev/tty.usbmodem167F364D3030',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=None)
def test1():
    print("connected to: " + ser.portstr)
    serialcmd= ("AT + ID"+"\r\n")
    ser.write(serialcmd.encode())
    response = ser.read(103)
    print(response)
    return response
def test2():
    num = 1
    cont = str(num)
    serialcmd1 = ("AT+CMSGHEX=" + cont)
    ser.write(serialcmd1.encode())
    time.sleep(1)
    num = 1 + num
    response = ser.read(60)
    print(response)
    return response
#ser.close()
while 1:
    response = test2()
