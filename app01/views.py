from django.shortcuts import render,HttpResponse,redirect
import qrcode,random,string,json,time
from django.conf import settings
from app01 import models
# Create your views here.
def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else:
        erweima=request.GET.get('mg')
        username=request.POST.get("username")
        password=request.POST.get("password")
        er_obj=models.Erweima.objects.filter(req=erweima).first()
        if er_obj.status:
            return HttpResponse("该二维码已失效")
        user_obj=models.User.objects.filter(username=username,password=password).first()
        if user_obj:
            er_obj.status=1
            er_obj.save()
            models.Login.objects.create(user=user_obj,erweima=er_obj)
            return HttpResponse("登录成功！！")
        else:
            return HttpResponse("用户名或密码不正确")

def index(request):
    return render(request,"index.html")
def erweima(request):
    if request.method=="GET":
        req="".join(random.sample(string.ascii_lowercase,10))
        print(req)
        img = qrcode.make(settings.LOGIN_URL+req)
        with open("static/img/%s.jpg"%req,"wb") as f:
            img.save(f)
        img_url=settings.IMG_URL+req+".jpg"
        res={"req":req,"url":img_url}
        models.Erweima.objects.create(req=req)
        return HttpResponse(json.dumps(res))
    else:
        req=request.POST.get("req")
        res={"status":True,"msg":None}
        erweima_obj = models.Erweima.objects.filter(req=req).first()
        timeArray = time.strptime(erweima_obj.create_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        now = int(time.time())
        if now>=timeStamp+erweima_obj.ctime+28800:
            res["status"]=False
            res["msg"]="该二维码已失效！"
        elif erweima_obj.status:
            head=models.Login.objects.filter(erweima_id=erweima_obj.id).values("user__head").first()
            head_url=settings.BASE_URL+head.get("user__head")
            res["msg"]=head_url
        return HttpResponse(json.dumps(res))