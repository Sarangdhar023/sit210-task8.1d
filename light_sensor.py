import smbus
import time

SENSOR = 0x23

MINIMUMPOWER = 0x00
MAXIMUMPOWER = 0x01
REFRESH = 0x07
high_resolution_0netime = 0X23 

bus = smbus.SMBus(1)

def photometric_intensity(location):
    result = ((location[1] + (256 *location[0]))/1.2)
    return result

def light():
    location = bus.read_i2c_block_data(SENSOR,high_resolution_0netime)
    value = photometric_intensity(location)
    return value
 
def  main():
    while True:
        Calc_Light = light()
        print (Calc_Light)

        if(Calc_Light >= 1200):
            print("Too bright")
        elif(Calc_Light >= 700 and Calc_Light < 1199):
            print("Bright")
        elif(Calc_Light >= 300 and Calc_Light < 699):
            print("Medium")    
        elif(Calc_Light < 50 and Calc_Light > 299):
            print("Dark")
        elif(Calc_Light < 49):
            print("Too Dark")
        
        time.sleep(0.5)
main ()
