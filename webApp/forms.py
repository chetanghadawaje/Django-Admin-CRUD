from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate


class Frm_login(forms.Form):
    username = forms.CharField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'type': 'text', 'required': 'true'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control ', 'type': 'password', 'required': 'true', 'autocomplete': 'off'}))

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        kwargs = {'username': username}
        try:
            user = User.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        user = authenticate(username=username, password=password)
        return user


class Frm_Category(forms.ModelForm):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'required': 'true',}))

    class Meta:
        model = category
        fields = '__all__'


class Frm_Tag(forms.ModelForm):
    name = forms.CharField(required=True, max_length=25, widget=forms.TextInput(attrs={
        'class': 'form-control', 'required': 'true',}))

    class Meta:
        model = tag
        fields = '__all__'


class Frm_Product(forms.ModelForm):
    category = forms.ModelChoiceField(required=True, queryset=category.objects.all(), widget=forms.Select(
        attrs={'class':'form-control', 'required': 'true'}))
    tag = forms.ModelChoiceField(required=True, queryset=tag.objects.all(), widget=forms.Select(
        attrs={'class':'form-control', 'required': 'true'}))
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control', 'required': 'true'}))
    description = forms.CharField(required=True, max_length=100, widget=forms.Textarea(attrs={
        'class': 'form-control', 'required': 'true', 'rows':'3'}))
    image = forms.FileField(widget=forms.FileInput(attrs={'required': 'true', 'accept': 'image/*'}))

    class Meta:
        model = product
        fields = '__all__'

