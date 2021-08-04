from ccapi import *


ip="192.168.1.9"
port=8080
c=Camera(ip,port)

def wait(seconds):
    date=datetime.datetime.utcnow()
    dt=datetime.timedelta(seconds=seconds)
    while datetime.datetime.utcnow()<date+dt:
        pass