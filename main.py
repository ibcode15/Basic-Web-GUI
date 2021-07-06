import webview
import time
import threading
html = """
<!DOCTYPE html>
<html>
<title>W3.CSS</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-teal.css">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<style>
body {font-family: "Roboto", sans-serif}
.w3-bar-block .w3-bar-item {
  padding: 16px;
  font-weight: bold;
}
.bar { 
font-family: Verdana,sans-serif;
font-size: 20px;
line-height: 0.5;
}
</style>
<body>
<script>
function unminimize() {
    pywebview.api.unminimize()
}

function minimize() {
    pywebview.api.minimize()
}
function close() {
    pywebview.api.close()
}

function Fullscreen() {
    pywebview.api.Fullscreen()
}


</script>
<div class="w3-bar w3-border w3-black bar pywebview-drag-region">
  <a href="javascript:close()" class="w3-bar-item w3-button w3-hover-red w3-right">&#10006;</a>
  <a href="javascript:Fullscreen()" class="w3-bar-item w3-button w3-hover-grey w3-right">&#10064;</a>
  <a href="javascript:minimize()" class="w3-bar-item w3-button w3-hover-grey w3-right">&#9473;</a>
</div>



</body>
</html>

"""
global windowdict
windowdict = {
    "Close": False,
    "Minimize": False,
    "Fullscreen": False,
    "BeforeFullscreenPos": None
    }
WindowObject = webview.create_window('test',html=html,frameless=True)
#help(WindowObject)
def API_Func(window):
    while True:
        
        time.sleep(0.1)
        if window.x == -32000:
            pass
        elif window.y <= -1: #or window.x == 335 or window.x == 1296:
            window.move(0,0)
            window.resize(1600, 860)
        elif window.x == 0 and window.y == 0 and window.height == 860 and window.width == 1600:
            pass
        elif window.height == 860 and window.width == 1600:
            window.resize(784, 561)
            window.move(windowdict["BeforeFullscreenPos"][0], windowdict["BeforeFullscreenPos"][1] + 500)
        else:
            
            windowdict["BeforeFullscreenPos"] = [window.x,window.y]
                
        for i in windowdict.keys():
            if i == "Close":
                if windowdict[i]:
                    window.destroy()
                    windowdict[i] = False
                    
            elif i == "Minimize":
                if windowdict[i]:
                    window.minimize()
                    windowdict[i] = False
            elif i == "Fullscreen":
                if windowdict[i]:
                    if window.height == 561:
                        window.move(0,0)
                        window.resize(1600, 860)
                    #elif window.height == 860:
                    #    window.move(0,0)
                    else:
                        window.resize(784, 561)
                        window.move(windowdict["BeforeFullscreenPos"][0], windowdict["BeforeFullscreenPos"][1])
                    windowdict[i] = False
            else:
                pass
        
class API:
    def __init__(self):
        self.fullscreen = False
    def minimize(self):
        windowdict["Minimize"] = True
    def close(self):
        windowdict["Close"] = True
    def Fullscreen(self):
        windowdict["Fullscreen"] = True
api = API()    
WindowObject._js_api = api
webview.start(API_Func, WindowObject)

