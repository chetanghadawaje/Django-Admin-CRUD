from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import product, tag, category
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.models import User


def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def loginView(request):
    form_data = request.POST
    form = Frm_login(form_data)
    if form.is_valid():
        try:
            user_obj = User.objects.get(username=request.POST["username"])
        except User.DoesNotExist:
            user_obj = None
        if user_obj != None:
            user = form.login(request)
            if user:
                login(request, user)
                return redirect('webapp:product')
            else:
                messages.success(request, "Enter Valid User Name and Password.")
                return render(request, 'login.html', {'form': form})
        else:
            messages.success(request, "Enter Valid User Name.")
            return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form})


def logoutView(request):
    logout(request)
    return redirect("webapp:login")


class categoryView(View):
    form_class = Frm_Category
    initial = {'key': 'value'}
    template_name = 'category.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        objects = category.objects.all()
        return render(request, self.template_name, {'form': form, 'objects': objects})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/category/')
        return render(request, self.template_name, {'form': form})


class tagView(View):
    form_class = Frm_Tag
    initial = {'key': 'value'}
    template_name = 'tag.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        objects = tag.objects.all()
        return render(request, self.template_name, {'form': form, 'objects': objects})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tag/')
        return render(request, self.template_name, {'form': form})


class productView(View):
    form_class = Frm_Product
    initial = {'key': 'value'}
    template_name = 'product.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        objects = product.objects.all()
        return render(request, self.template_name, {'form': form, 'objects': objects})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/product/')
        return render(request, self.template_name, {'form': form})