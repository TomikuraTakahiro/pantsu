from django import forms
from .models import sake
from django.contrib.auth.forms import (
    AuthenticationForm
)

class SearchSakeForm(forms.ModelForm):
    """酒検索のフォーム"""
    class Meta:
        model = sake
        fields = ('name','creater','region','created_type','sake_type','dosu','karasa')

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
