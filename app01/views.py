from django.shortcuts import render, HttpResponse
from utils.twilio.sms import send_single_sms
import random
from django import forms
from app01 import models


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


class RegisterModelForm(forms.ModelForm):
    # rewrite the UserInfo field
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    # add fields
    confirm_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    code = forms.CharField(label="Verification Code")

    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        # change the field sequence
        fields = ['username','email','password','confirm_password','mobile_phone','code']
    def __init__(self):
        super().__init__()
        print(self.fields)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = "Please Input " + field.label
            print(field.label)

def register(request):
    form = RegisterModelForm()
    return render(request, "app01/register.html", {'form': form})
