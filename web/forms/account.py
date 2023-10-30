from django import forms
from web import models


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
        fields = ['username', 'email', 'password', 'confirm_password', 'mobile_phone', 'code']

    def __init__(self):
        super().__init__()
        print(self.fields)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = "form-control"
            field.widget.attrs['placeholder'] = "Please Input " + field.label
            print(field.label)
