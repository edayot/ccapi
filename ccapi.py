import requests
import json
import datetime
from email.utils import formatdate
from PIL import Image
from io import BytesIO






class Camera:
    def __init__(self,ip,port):
        Camera.url="http://"+ip+":"+str(port)+"/ccapi"
        Camera.rtpurl="rtp://"+ip+":"+str(port)+"/media"

    def get(self):
        return requests.get(Camera.url).json()
    class deviceinformation:
        def get():
            return requests.get(Camera.url+"/ver100/deviceinformation").json()
    
    
    class devicestatus:
        class battery:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/battery").json()
        class storage:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/storage").json()
        class lens:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/lens").json()
        class temperature:
            def get():
                return requests.get(Camera.url+"/ver100/devicestatus/battery").json()
    
    class functions:
        class registeredname:
            class copyright:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/copyright").json()
                def put(copyright):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/copyright",json={"copyright":copyright}).json()
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/copyright").json()
            class author:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/author").json()
                def put(author):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/author",json={"author":author}).json()
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/author").json()
            class ownername:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/ownername").json()
                def put(ownername):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/ownername",json={"ownername":ownername}).json()
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/ownername").json()
            class nickname:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/nickname").json()
                def put(nickname):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/nickname",json={"nickname":nickname}).json()
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/nickname").json()
            class copyright:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/registeredname/copyright").json()
                def put(copyright):
                    return requests.put(Camera.url+"/ver100/functions/registeredname/copyright",json={"copyright":copyright}).json()
                def delete():
                    return requests.delete(Camera.url+"/ver100/functions/registeredname/copyright").json()
        class datetime:
            def get():
                return requests.get(Camera.url+"/ver100/functions/datetime").json()
            def put(datetime,dst):
                return requests.put(Camera.url+"/ver100/functions/datetime",json={"datetime":datetime,"dst":dst}).json()
            def sync():
                Camera.functions.datetime.put(formatdate(timeval=None, localtime=True, usegmt=False),False)
        class cardformat:
            def post(name):
                r=input("Please confirm by typing yes : ")
                if r=="yes":
                    print("Formating")
                    return requests.post(Camera.url+"/ver100/functions/cardformat",json={"name":name}).json()
                else:
                    return None
        class beep:
            def get():
                return requests.get(Camera.url+"/ver100/functions/beep").json()
            def put(value):
                return requests.put(Camera.url+"/ver100/functions/beep",json={"value":value}).json()
        class autopoweroff:
            def get():
                return requests.get(Camera.url+"/ver100/functions/autopoweroff").json()
            def put(value):
                return requests.put(Camera.url+"/ver100/functions/autopoweroff",json={"value":value}).json()
        class wificonnection:
            def post(value):
                return requests.put(Camera.url+"/ver100/functions/wificonnection",json={"value":value}).json()
        class wifisetting:
            def get():
                return requests.get(Camera.url+"/ver100/functions/wifisetting").json()
            class set1:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/wifisetting/set1").json()
                def put(body):
                    """
                    Put a json body like the .get() method
                    """
                    return requests.put(Camera.url+"/ver100/functions/wifisetting/set1",json=body).json()
            class set2:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/wifisetting/set2").json()
                def put(body):
                    """
                    Put a json body like the .get() method
                    """
                    return requests.put(Camera.url+"/ver100/functions/wifisetting/set2",json=body).json()
            class set3:
                def get():
                    return requests.get(Camera.url+"/ver100/functions/wifisetting/set3").json()
                def put(body):
                    """
                    Put a json body like the .get() method
                    """
                    return requests.put(Camera.url+"/ver100/functions/wifisetting/set3",json=body).json()
    class contents:
        def display(path):
            r=Camera.contents.get_file(path)
            img = Image.open(BytesIO(r.content))
            img.show()
        def get_directory(path):
            '''
            path is the path of a directory: "/sd/100CANON"
            '''
            return requests.get(Camera.url+"/ver100/contents"+path).json()
        def get_file(path):
            '''
            path is the path of a file: "/sd/100CANON/IMG_0000.JPG"
            '''
            return requests.get(Camera.url+"/ver100/contents"+path)
            
        def get_chunked(path):
            '''
            path is the path of a directory : "/sd/100CANON"
            '''
            r=requests.get(Camera.url+"/ver100/contents"+path+"?kind=chunked")
            j=json.loads("["+r.text.replace('{"url"',',{"url"')[1:]+"]")
            result={"url":[]}
            for page in j:
                for url in page["url"]:
                    result["url"].append(url)
            return result
    class shooting:
        class control:
            class shutterbutton():
                def post(af):
                    return requests.post(Camera.url+"/ver100/shooting/control/shutterbutton",json={"af":af}).json()
                class manual:
                    def post(action,af):
                        return requests.post(Camera.url+"/ver100/shooting/control/shutterbutton/manual",json={"action":action,"af":af}).json()
            class moviemode:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/control/moviemode").json()
                def post(status):
                    return requests.post(Camera.url+"/ver100/shooting/control/moviemode",json={"status":status}).json()
            class recbutton:
                def post(action):
                    return requests.post(Camera.url+"/ver100/shooting/control/moviemode",json={"action":action}).json()
            class drivefocus:
                def post(value):
                    return requests.post(Camera.url+"/ver100/shooting/control/drivefocus",json={"value":value}).json()
            class af:
                def post(action):
                    return requests.post(Camera.url+"/ver100/shooting/control/af",json={"action":action}).json()
        class settings:
            def get():
                return requests.get(Camera.url+"/ver100/shooting/settings").json()
            class shootingmodedial:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/settings/shootingmodedial").json()
            class afoperation:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/settings/afoperation").json()

            class __single__:
                def __init__(self,url):
                    self.url=url
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def put(self,value):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":value}).json()
                def change(self,n):
                    """ 
                    increase/decrease value by n in ability
                    """
                    r=self.get()
                    return self.put(r["ability"][(r["ability"].index(r["value"])+n)%len(r["ability"])])
            class __single_step__:
                def __init__(self,url):
                    self.url=url
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def put(self,value):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":value}).json()
                def change(self,n):
                    """ 
                    increase/decrease value by n*step in ability 
                    """
                    r=self.get()
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
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def put(self,var1,var2):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":{self.var1:var1,self.var2:var2}}).json()
                def change(self,n,m):
                    """ 
                    increase/decrease value by n,m in ability (the two are changed)
                    """
                    
                    r=self.get()
                    var1=r["ability"][self.var1][(r["ability"][self.var1].index(r["value"][self.var1])+n)%len(r["ability"][self.var1])]
                    var2=r["ability"][self.var2][(r["ability"][self.var2].index(r["value"][self.var2])+m)%len(r["ability"][self.var2])]
                    return self.put(var1,var2)
            class __double_step__:
                def __init__(self,url,var1,var2):
                    self.url=url
                    self.var1=var1
                    self.var2=var2
                def get(self):
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def put(self,var1,var2):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":{self.var1:var1,self.var2:var2}}).json()
                def change(self,n,m):
                    """ 
                    increase/decrease value by n*step,m*step in ability (the two are changed)
                    """
                    r=self.get()
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
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def put(self,var1,var2,var3,var4,var5,var6):
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json={"value":{self.var1:var1,self.var2:var2,self.var3:var3,self.var4:var4,self.var5:var5,self.var6:var6}}).json()
                def delete(self):
                    return requests.delete(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def change(self,n,m,o,p,q,a):
                    """ 
                    increase/decrease value by n*step,m*step in ability (the two are changed)
                    """
                    r=self.get()
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
                        return requests.get(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def put(self,basepicturestyle,var1,var2,var3,var4,var5,var6):
                    j={"value":{"basepicturestyle":basepicturestyle,self.var1:var1,self.var2:var2,self.var3:var3,self.var4:var4,self.var5:var5,self.var6:var6}}
                    return requests.put(Camera.url+"/ver100/shooting/settings"+self.url,json=j).json()
                def delete(self):
                    return requests.delete(Camera.url+"/ver100/shooting/settings"+self.url).json()
                def change(self,n,m,o,p,q,a):
                    """ 
                    increase/decrease value by n*step,m*step in ability (the two are changed)
                    """
                    r=self.get()
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
                    return requests.get(Camera.url+"/ver100/shooting/information/recordable").json()






        
            
            

        class liveview:
            def get():
                return {"ability":{"liveviewsize":["off","small","medium"],"cameradisplay":["on","off","keep"]}}
            def post(liveviewsize,cameradisplay):
                return requests.post(Camera.url+"/ver100/shooting/liveview",json={"liveviewsize":liveviewsize,"cameradisplay":cameradisplay}).json()
            class flip:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/flip").content
                def save(path="ouput.jfif"):
                    "same as get method but save the image as path"
                    with open(path,"wb") as f:
                        f.write(requests.get(Camera.url+"/ver100/shooting/liveview/flip").content)
            class flipdetail:
                def get(kind="info"):
                    r=requests.get(Camera.url+"/ver100/shooting/liveview/flipdetail/?kind="+kind)
                    if kind=="info":
                        return int.from_bytes(r.content[3:7],"big"),json.loads(r.text[7:len(r.text)-2])
                    elif kind=="image":
                        return int.from_bytes(r.content[3:7],"big"),r.content[7:-2]
                    elif kind=="both":
                        i=r.content.index(b'\xff\x00\x00')
                        return [(int.from_bytes(r.content[3:7],"big"),json.loads(r.text[7:i-2])),(int.from_bytes(r.content[i+3:i+7],"big"),r.content[i+7:-2])]
                    else:
                        return r
            class scroll:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/scroll").content
                def delete():
                    return requests.delete(Camera.url+"/ver100/shooting/liveview/scroll").content
                    
                    
            class rtp:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/rtp").json()
                def post(ip,action):
                    return requests.post(Camera.url+"/ver100/shooting/liveview/rtp",json={"ipaddress":ip,"action":action}).json()
            class rtpsessiondesc:
                def get():
                    return requests.get(Camera.url+"/ver100/shooting/liveview/rtpsessiondesc").text
                

                
                
                
ip="192.168.1.9"
port=8080
c=Camera(ip,port) 
        
