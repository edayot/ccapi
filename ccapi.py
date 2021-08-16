import requests
import json
import datetime
from email.utils import formatdate
from io import BytesIO






class Camera:
    def __init__(self,ip,port):
        Camera.url="http://"+ip+":"+str(port)+"/ccapi"
        Camera.rtpurl="rtp://"+ip+":"+str(port)+"/media"

    def get(self):
        return requests.get(Camera.url)
    class deviceinformation:
        def get():
            return requests.get(Camera.url+"/ver100/deviceinformation")
    
    
    class devicestatus:
        class battery:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/battery")
        class storage:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/storage")
        class lens:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/lens")
        class temperature:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/battery")
    
    class functions:
        class registeredname:
            class copyright:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/copyright")
                def put(copyright):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/copyright",json={"copyright":copyright})
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/copyright")
            class author:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/author")
                def put(author):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/author",json={"author":author})
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/author")
            class ownername:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/ownername")
                def put(ownername):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/ownername",json={"ownername":ownername})
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/ownername")
            class nickname:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/nickname")
                def put(nickname):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/nickname",json={"nickname":nickname})
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/nickname")
            class copyright:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/copyright")
                def put(copyright):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/copyright",json={"copyright":copyright})
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/copyright")
        class datetime:
            def get():
                return requests.get(Camera.url+"/ver100/functions/datetime")
            def put(datetime,dst):
                return requests.put(Camera.url+"/ver100/functions/datetime",json={"datetime":datetime,"dst":dst})
            def sync():
                Camera.functions.datetime.put(formatdate(timeval=None, localtime=True, usegmt=False),False)
        class cardformat:
            def post(name):
                r=input("Please confirm by typing yes : ")
                if r=="yes":
                    print("Formating")
                    return requests.post(Camera.url+"/ver100/functions/cardformat",json={"name":name})
                else:
                    return None
        class beep:
            def get():
                return requests.get(Camera.url+"/ver100/functions/beep")
            def put(value):
                return requests.put(Camera.url+"/ver100/functions/beep",json={"value":value})
        class autopoweroff:
            def get():
                return requests.get(Camera.url+"/ver100/functions/autopoweroff")
            def put(value):
                return requests.put(Camera.url+"/ver100/functions/autopoweroff",json={"value":value})
        class wificonnection:
            def post(value):
                return requests.put(Camera.url+"/ver100/functions/wificonnection",json={"value":value})
        class wifisetting:
            def get():
                return requests.get(Camera.url+"/ver100/functions/wifisetting")
            class set1:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/wifisetting/set1")
                def put(body):
                    """
                    Put a json body like the .get() method
                    """
                    return requests.put(Camera.url+"/ver100/functions/wifisetting/set1",json=body)
            class set2:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/wifisetting/set2")
                def put(body):
                    """
                    Put a json body like the .get() method
                    """
                    return requests.put(Camera.url+"/ver100/functions/wifisetting/set2",json=body)
            class set3:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/wifisetting/set3")
                def put(body):
                    """
                    Put a json body like the .get() method
                    """
                    return requests.put(Camera.url+"/ver100/functions/wifisetting/set3",json=body)
    class contents:
        def get(path):
            '''
            path is the path of a file: "/sd/100CANON/IMG_0000.JPG"
            '''
            return requests.get(Camera.url+"/ver100/contents"+path)
    class shooting:
        class control:
            class shutterbutton():
                def post(af):
                    return requests.post(Camera.url+"/ver100/shooting/control/shutterbutton",json={"af":af})
                class manual:
                    def post(action,af):
                        return requests.post(Camera.url+"/ver100/shooting/control/shutterbutton/manual",json={"action":action,"af":af})
            class moviemode:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/control/moviemode")
                def post(status):
                    return requests.post(Camera.url+"/ver100/shooting/control/moviemode",json={"status":status})
            class recbutton:
                def post(action):
                    return requests.post(Camera.url+"/ver100/shooting/control/moviemode",json={"action":action})
            class drivefocus:
                def post(value):
                    return requests.post(Camera.url+"/ver100/shooting/control/drivefocus",json={"value":value})
            class af:
                def post(action):
                    return requests.post(Camera.url+"/ver100/shooting/control/af",json={"action":action})
        class settings:
            def get():
                return requests.get(Camera.url+"/ver100/shooting/settings")
            class shootingmodedial:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/settings/shootingmodedial")
            class afoperation:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/settings/afoperation")

            class __single__:
                def __init__(self,url):
                    self.url=url
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url)
                def put(self,value):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":value})
                def change(self,n):
                    """ 
                    increase/decrease value by n in ability
                    """
                    r=self.get().json()
                    return self.put(r["ability"][(r["ability"].index(r["value"])+n)%len(r["ability"])])
            class __single_step__:
                def __init__(self,url):
                    self.url=url
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url)
                def put(self,value):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":value})
                def change(self,n):
                    """ 
                    increase/decrease value by n*step in ability 
                    """
                    r=self.get().json()
                    step=r["ability"]["step"]
                    min_=r["ability"]["min"]
                    max_=r["ability"]["max"]
                    value=(r["value"]+n*step)%(max_-min_)-min_
                    return self.put(value)
            

            class __double__:
                def __init__(self,url,var1,var2):
                    self.url=url
                    self.var1=var1
                    self.var2=var2
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url)
                def put(self,var1,var2):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":{self.var1:var1,self.var2:var2}})
                def change(self,n,m):
                    """ 
                    increase/decrease value by n,m in ability (the two are changed)
                    """
                    
                    r=self.get().json()
                    var1=r["ability"][self.var1][(r["ability"][self.var1].index(r["value"][self.var1])+n)%len(r["ability"][self.var1])]
                    var2=r["ability"][self.var2][(r["ability"][self.var2].index(r["value"][self.var2])+m)%len(r["ability"][self.var2])]
                    return self.put(var1,var2)
            class __double_step__:
                def __init__(self,url,var1,var2):
                    self.url=url
                    self.var1=var1
                    self.var2=var2
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url)
                def put(self,var1,var2):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":{self.var1:var1,self.var2:var2}})
                def change(self,n,m):
                    """ 
                    increase/decrease value by n*step,m*step in ability (the two are changed)
                    """
                    r=self.get().json()
                    step1=r["ability"][self.var1]["step"]
                    step2=r["ability"][self.var2]["step"]

                    min1=r["ability"][self.var1]["min"]
                    min2=r["ability"][self.var2]["min"]

                    max1=r["ability"][self.var1]["max"]
                    max2=r["ability"][self.var2]["max"]

                    var1=(r["value"][self.var1]+n*step1)%(max1-min1)-min1
                    var2=(r["value"][self.var2]+m*step2)%(max2-min2)-min2


                    return self.put(var1,var2)

            class __sextuple_step__:
                def __init__(self,url,var1,var2,var3,var4,var5,var6):
                    self.url=url
                    self.var1=var1
                    self.var2=var2
                    self.var3=var3
                    self.var4=var4
                    self.var5=var5
                    self.var6=var6
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url)
                def put(self,var1,var2,var3,var4,var5,var6):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":{self.var1:var1,self.var2:var2,self.var3:var3,self.var4:var4,self.var5:var5,self.var6:var6}})
                def delete(self):
                    return requests.delete(Camera.url+"/ver100/shooting/settings"+self.url)
                def change(self,n,m,o,p,q,a):
                    """ 
                    increase/decrease value by n*step,m*step in ability (the two are changed)
                    """
                    r=self.get().json()
                    step1=r["ability"][self.var1]["step"]
                    step2=r["ability"][self.var2]["step"]
                    step3=r["ability"][self.var3]["step"]
                    step4=r["ability"][self.var4]["step"]
                    step5=r["ability"][self.var5]["step"]
                    step6=r["ability"][self.var6]["step"]
                    

                    min1=r["ability"][self.var1]["min"]
                    min2=r["ability"][self.var2]["min"]
                    min3=r["ability"][self.var3]["min"]
                    min4=r["ability"][self.var4]["min"]
                    min5=r["ability"][self.var5]["min"]
                    min6=r["ability"][self.var6]["min"]

                    max1=r["ability"][self.var1]["max"]
                    max2=r["ability"][self.var2]["max"]
                    max3=r["ability"][self.var3]["max"]
                    max4=r["ability"][self.var4]["max"]
                    max5=r["ability"][self.var5]["max"]
                    max6=r["ability"][self.var6]["max"]

                    var1=(r["value"][self.var1]+n*step1-min1)%(max1-min1)+min1
                    var2=(r["value"][self.var2]+m*step2-min2)%(max2-min2)+min2
                    var3=(r["value"][self.var3]+o*step3-min3)%(max3-min3)+min3
                    var4=(r["value"][self.var4]+p*step4-min4)%(max4-min4)+min4
                    var5=(r["value"][self.var5]+q*step5-min5)%(max5-min5)+min5
                    var6=(r["value"][self.var6]+a*step6-min6)%(max6-min6)+min6

                    return self.put(var1,var2,var3,var4,var5,var6)
            class __septuple__:
                def __init__(self,url,var1,var2,var3,var4,var5,var6):
                    self.url=url
                    self.var1=var1
                    self.var2=var2
                    self.var3=var3
                    self.var4=var4
                    self.var5=var5
                    self.var6=var6
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url)
                def put(self,basepicturestyle,var1,var2,var3,var4,var5,var6):
                    j={"value":{"basepicturestyle":basepicturestyle,self.var1:var1,self.var2:var2,self.var3:var3,self.var4:var4,self.var5:var5,self.var6:var6}}
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json=j)
                def delete(self):
                    return requests.delete(Camera.url+"/ver100/shooting/settings"+self.url)
                def change(self,n,m,o,p,q,a):
                    """ 
                    increase/decrease value by n*step,m*step in ability (the two are changed)
                    """
                    r=self.get().json()
                    step1=r["ability"][self.var1]["step"]
                    step2=r["ability"][self.var2]["step"]
                    step3=r["ability"][self.var3]["step"]
                    step4=r["ability"][self.var4]["step"]
                    step5=r["ability"][self.var5]["step"]
                    step6=r["ability"][self.var6]["step"]
                    

                    min1=r["ability"][self.var1]["min"]
                    min2=r["ability"][self.var2]["min"]
                    min3=r["ability"][self.var3]["min"]
                    min4=r["ability"][self.var4]["min"]
                    min5=r["ability"][self.var5]["min"]
                    min6=r["ability"][self.var6]["min"]

                    max1=r["ability"][self.var1]["max"]
                    max2=r["ability"][self.var2]["max"]
                    max3=r["ability"][self.var3]["max"]
                    max4=r["ability"][self.var4]["max"]
                    max5=r["ability"][self.var5]["max"]
                    max6=r["ability"][self.var6]["max"]

                    var1=(r["value"][self.var1]+n*step1-min1)%(max1-min1)+min1
                    var2=(r["value"][self.var2]+m*step2-min2)%(max2-min2)+min2
                    var3=(r["value"][self.var3]+o*step3-min3)%(max3-min3)+min3
                    var4=(r["value"][self.var4]+p*step4-min4)%(max4-min4)+min4
                    var5=(r["value"][self.var5]+q*step5-min5)%(max5-min5)+min5
                    var6=(r["value"][self.var6]+a*step6-min6)%(max6-min6)+min6

                    basepicturestyle=r["value"]["basepicturestyle"]

                    return self.put(basepicturestyle,var1,var2,var3,var4,var5,var6)
            

            av=__single__("/av")
            tv=__single__("/tv")
            iso=__single__("/iso")
            exposure=__single__("/exposure")
            wb=__single__("/wb")
            afmethod=__single__("/afmethod")
            stillimagequality=__double__("/stillimagequality","raw","jpeg")
            flash=__single__("/flash")
            metering=__single__("/metering")
            drive=__single__("/drive")
            aeb=__single__("/aeb")
            wbshift=__double_step__("/wbshift","ba","mg")
            wbbracket=__single__("/wbbracket")
            colorspace=__single__("/colorspace")
            picturestyle=__single__("/picturestyle")

            for t in ["auto","standard","portrait","landscape","finedetail","neutral","faithful","monochrome"]:
                exec("picturestyle."+t+'=__sextuple_step__("/picturestyle/'+t+'","sharpness_strength","sharpness_fineness","sharpness_threshold","contrast","saturation","colortone")')

            for t in ["userdef1","userdef2","userdef3"]:
                exec("picturestyle."+t+'=__septuple__("/picturestyle/'+t+'","sharpness_strength","sharpness_fineness","sharpness_threshold","contrast","saturation","colortone")')
                exec("picturestyle."+t+'.basepicturestyle=__single__("/picturestyle/'+t+'/basepicturestyle")')

            moviequality=__single__("/moviequality")
            soundrecording=__single__("/soundrecording")
            
            soundrecording.level=__single_step__("/soundrecording/level")
            soundrecording.windfilter=__single__("/soundrecording/windfilter")
            soundrecording.attenuator=__single__("/soundrecording/attenuator")

        class information:
            class recordable:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/information/recordable")

            

        class liveview:
            def get():
                return {"ability":{"liveviewsize":["off","small","medium"],"cameradisplay":["on","off","keep"]}}
            def post(liveviewsize,cameradisplay):
                return requests.post(Camera.url+"/ver100/shooting/liveview",json={"liveviewsize":liveviewsize,"cameradisplay":cameradisplay})
            class flip:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/flip")
            class flipdetail:
                def get(kind="info"):
                    return requests.get(Camera.url+"/ver100/shooting/liveview/flipdetail/?kind="+kind)
            class scroll:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/scroll",stream=True)
                def delete():
                    return requests.delete(Camera.url+"/ver100/shooting/liveview/scroll",stream=True)
            class scrolldetail:
                def get(kind):
                    return requests.get(Camera.url+"/ver100/shooting/liveview/scrolldetail?kind="+kind,stream=True)
                def delete():
                    return requests.delete(Camera.url+"/ver100/shooting/liveview/scrolldetail")
                    
            class rtp:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/rtp")
                def post(ip,action):
                    return requests.post(Camera.url+"/ver100/shooting/liveview/rtp",json={"ipaddress":ip,"action":action})
            class rtpsessiondesc:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/rtpsessiondesc")
            class angleinformation:
                def get():
                    return {"ability":{"action":["start","stop"]}}
                def post(action):
                    return requests.post(Camera.url+"/ver100/shooting/liveview/angleinformation",json={"action":action})
            class afframeposition:
                def put(positionx,positiony):
                    requests.put(Camera.url+"/ver100/shooting/liveview/afframeposition",json={"positionx":positionx,"positiony":positiony})
            
    class event:
        class polling:
            def get(continue_):
                return requests.get(Camera.url+"/ver100/event/polling?continue="+continue_)
            def delete():
                return requests.delete(Camera.url+"/ver100/event/polling")
        class monitoring:
            def get(continue_):
                return requests.get(Camera.url+"/ver100/event/monitoring?continue="+continue_)
            def delete():
                return requests.delete(Camera.url+"/ver100/event/monitoring")


class decode:
    def __init__(self,data):
        self.data=data
        self.data_decoded=[]
        while data!=b"":
            i=int.from_bytes(data[3:7],"big")
            self.data_decoded.append({"bytesize":i,"type":data[2],"data":data[7:7+i]})
            data=data[9+i:]



def save(bytes_str,path="output.jfif"):
    with open(path,"wb") as f:
        f.write(bytes_str)


if __name__ == "__main__":              
    ip="192.168.1.19"
    port=8080
    c=Camera(ip,port) 
        
