from django.shortcuts import render, HttpResponse
import base64, cv2
import numpy as np
import matplotlib.pyplot as plt
from .models import insert






# Create your views here.
def home(request):
    return render(request, "chat_home.html")

def singup(request):
    if request.POST:
        insert()
        if request.POST.get('name') and request.POST.get('img'):
            
            return HttpResponse("ok")
        else:
            return HttpResponse('no value')
    return render(request, "signup.html")

def login(request):
    if request.POST:
        imgdata = base64.b64decode(request.POST.get('imageData').split(',')[-1])
        
        # 測試 儲存圖片
        # filename = "chat/faceimgs/videoshot.jpg"
        # with open(filename, "wb") as f:
        #     f.write(imgdata)
        
        # 測試 直接顯示相片
        nparr = np.frombuffer(imgdata, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        # OpenCV 是 BGR 模式。但是 Matplotib 是 RGB 模式，所以需要用將BGR轉RGB才能用 Matplotib呈現
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.show()
        
        
        return HttpResponse('ok')
    return render(request, "login.html")

def chatroom(request):
    return render(request, "chatroom.html")