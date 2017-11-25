from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from index.models import User
from index.forms import UserForm


# Create your views here.
def index(request):

    if 'id' in request.session.keys():
        return render(request, 'index/home.html')
    else:
        return redirect('/sign_in/')


def sign_in(request):

    if request.method == 'POST':
        data = request.POST

        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        login(request, user)

        if user is not None:
            request.session['id'] = user.id
            return redirect('/')

        else:
            return redirect('sign_in/')
    else:
        return render(request, 'index/sign_in.html')

def logout(request):

    del request.session['id']

    return redirect('/sign_in/')


def create_user(request):

    if request.method == 'POST':
        data = request.POST

        new_user = User.objects.create_user(
            username=data['username'],
            first_name = data['first_name'],
            last_name = data['username'],
            password = data['password'],
            email = data['email'],
            phonenumber = data['phone_number'],
            datebirth=None,
            gender=None
        )

        login(request, new_user)

        # a hack that maybe can be prevented with login
        request.session['id'] = new_user.id
        return redirect('/')


    else:
        return render(request, 'index/sign_up.html')
