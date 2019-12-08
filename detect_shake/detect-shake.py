import smbus
import time
import math


class DetectShake():
    
    def __init__(self):

        self.DEV_ADDR=0x68

        self.ACCEL_XOUT=0x3b
        self.ACCEL_YOUT=0x3d
        self.ACCEL_ZOUT=0x3f
        self.TEMP_OUT=0x41
        self.GYRO_XOUT=0x43
        self.GYRO_YOUT=0x45
        self.GYRO_ZOUT=0x47

        self.PWR_MGMT_1=0x6b
        self.PWR_MGMT_2=0x6c

        # Get I2C bus
        self.bus = smbus.SMBus(1)


        self.bus.write_byte_data(self.DEV_ADDR, self.PWR_MGMT_1, 0)


    def read_word(self,adr):
        high=self.bus.read_byte_data(self.DEV_ADDR,adr)
        low=self.bus.read_byte_data(self.DEV_ADDR,adr+1)
        val=(high<<8)+low
        return val

    def read_word_sensor(self,adr):
        val=read_word(adr)
        if (val>=0x8000):
            return -((65535-val)+1)
        else:
            return val
        
    def get_temp():
        temp=read_word_sensor(self.TEMP_OUT)
        x=temp/340+36.53
        return x

    def getGyro():
        x=read_word_sensor(self.GYRO_XOUT)/131.0
        y=read_word_sensor(self.GYRO_YOUT)/131.0
        z=read_word_sensor(self.GYRO_ZOUT)/131.0
        return [x,y,z]

    def getAccel():
        x=read_word_sensor(self.ACCEL_XOUT)/16384.0
        y=read_word_sensor(self.ACCEL_YOUT)/16384.0
        z=read_word_sensor(self.ACCEL_ZOUT)/16384.0
        return [x,y,z]
