from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.views import View

from users.forms import SignupForm, LoginForm

User = get_user_model()

class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, "Account created successfully")
            return redirect('login')
        return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()

        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('get_weather_detail')
            else:
                messages.error(request, "Invalid username or password.")

        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Logged out successfully!")
        return redirect('login')
    
