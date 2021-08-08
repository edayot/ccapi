import importlib
import ccapi
import datetime
import time
importlib.reload(ccapi)


ip="192.168.1.18"
port=8080
c=ccapi.Camera(ip,port)


def take_liveview_picture():
    c.shooting.liveview.flip.save()

def intervallometer(Camera,shots,interval):
    def take_picture():
        r=Camera.shooting.control.shutterbutton.post(af=False)
        print("Picture "+str(i)+"/"+str(shots)+" : status_code="+str(r.status_code)+" current="+time.ctime(start+interval*i))
    start=time.time()
    i=1
    take_picture()
    while i<shots:
        while time.time()<start+interval*i:
            pass
        i=i+1
        take_picture()
        

