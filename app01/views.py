from django.shortcuts import render, HttpResponse
from utils.twilio.sms import send_single_sms
import random


# Create your views here.
def send_sms(request):
    code = random.randrange(1000, 9999)

    tpl = request.GET.get('tpl')

    if tpl == "login":
        content = "Login Code: " + str(code)
    elif tpl == "register":
        content = "Register Code: " + str(code)
    else:
        return HttpResponse("SMS Template Not Exist!")

    try:
        res = send_single_sms(content)
    except Exception as e:
        print(str(e))
        return HttpResponse(str(e))

    # print(res)
    return HttpResponse("Success!")
