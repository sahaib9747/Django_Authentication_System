from django.contrib import auth
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        if 'reg-submit' in request.POST: 
            username = request.POST['username']
            first_name = request.POST['first-name']
            last_name = request.POST['last-name']
            email = request.POST['email']
            password = request.POST['password']
            con_password = request.POST['cont-password']

            if password == con_password:
                # check username existency
                if User.objects.filter(username=username).exists():
                    messages.warning(request, 'Username already exists')
                elif User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                else:
                    new_user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)

                    # automatic login 
                    login(request, new_user)
                    return redirect('/accounts/')
        elif 'login-submit' in request.POST:
            username = request.POST['username']
            passowrd = request.POST['password']
            
            log_status = authenticate(username=username, passowrd=passowrd)

            if log_status is not None:
                login(request, log_status)
            else:
                messages.error(request, 'Wrong credentials!!')
                return redirect('/accounts/')
        elif 'logout-submit' in request.POST:
            logout(request)
            return redirect('/accounts/')
        else:
            pass

    return render(request, 'index.html')
