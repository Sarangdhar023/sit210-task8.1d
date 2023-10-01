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
        lux = light()
        print (lux)

        if(lux >= 1200):
            print("Too bright")
        elif(lux >= 700 and lux < 1199):
            print("Bright")
        elif(lux >= 300 and lux < 699):
            print("Medium")    
        elif(lux < 50 and lux > 299):
            print("Dark")
        elif(lux < 49):
            print("Two Dark")
        
        time.sleep(0.5)
main ()
