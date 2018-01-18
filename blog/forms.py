from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField


class ContactForm(forms.Form):
    cst = {
        'class': 'form-control cst__radius',
        'required': 'required'
    }
    邮箱 = forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs=cst)
    )
    摘要 = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs=cst)
    )
    信息 = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs=cst)
    )
    # captcha = NoReCaptchaField()
