from django import forms
from .models import Contact
from captcha.fields import ReCaptchaField

class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Contact
        fields = ("email","captcha")
        widgets = {
            "email" : forms.TextInput(attrs = {"class": "editContent", "placeholder": "Your Email..."})
        }
        labels = {
            "email": ''
        }