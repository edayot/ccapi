import importlib
import ccapi
import datetime
importlib.reload(ccapi)


ip="192.168.1.9"
port=8080
c=ccapi.Camera(ip,port)

def wait(seconds):
    date=datetime.datetime.utcnow()
    dt=datetime.timedelta(seconds=seconds)
    while datetime.datetime.utcnow()<date+dt:
        pass

def take_liveview_picture():
    c.shooting.liveview.flip.save()