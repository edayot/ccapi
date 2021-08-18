import importlib
import ccapi
import time
import socket
import requests
from PIL import Image  
importlib.reload(ccapi)


ip="192.168.1.9"
port=8080
c=ccapi.Camera(ip,port)


def take_liveview_picture():
    c.shooting.liveview.flip.save()

def display_last_image(Camera):
    r2=Camera.event.polling.get("off")
    r=requests.get(r2.json()["addedcontents"][1])
    ccapi.save(r.content,"temp/output.jpeg")
    img=Image.open("temp/output.jpeg")
    img.show()


def intervallometer(Camera,shots,interval,wait=False,display=False):
    def take_picture():
        r=Camera.shooting.control.shutterbutton.post(af=False)
        if display:
            time.sleep(0.1)
            display_last_image(Camera)
            

        print("Picture "+str(i)+"/"+str(shots)+" : status_code="+str(r.status_code)+" current="+time.ctime(start+interval*i))
        
    print(c.devicestatus.battery.get())
    start=time.time()
    i=0
    if wait:
        i=1
        take_picture()
    while i<shots:
        while time.time()<start+interval*i:
            pass
        i=i+1
        take_picture()


def chunk_get():
    c.shooting.liveview.post("medium","off")
    r=c.shooting.liveview.scrolldetail.get("image")
    print("Requested")
    t=time.time()
    while time.time()<t+5:
        pass
    print("Passed")
    
    #c.shooting.liveview.scrolldetail.delete()
    print("Deleted")
    c.shooting.liveview.post("off","off")
    return r

def polling_battery():
    r1=c.shooting.settings.tv.get()
    r2=c.event.polling.get("off")
    return r1,r2


def start_rtp():
    c.shooting.liveview.post("small","on")
    time.sleep(0.25)
    r=c.shooting.liveview.rtpsessiondesc.get()
    with open("sdp.sdp","w") as f: #Can be open with VLC
        f.write(r.text)
    c.shooting.liveview.rtp.post(socket.gethostbyname(socket.gethostname()),"start")
    print(r.text)

def stop_rtp():
    c.shooting.liveview.rtp.post(socket.gethostbyname(socket.gethostname()),"stop")