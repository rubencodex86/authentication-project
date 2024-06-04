from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib import messages
import re
from django.contrib.auth import authenticate, login, logout


def register(request):
    register_form = RegisterUserForm()

    if request.method == "POST":
        register_form = RegisterUserForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password1')
        username = request.POST.get('username')

        if email == '':
            messages.error(request, 'You must enter a valid e-mail address')

        if username == '':
            messages.error(request, 'The username field cannot be empty')

        if not re.search(r'\d', password):
            messages.error(request, 'Error: Password must contain at least one number!')
            return render(request, 'register.html', {'form': register_form})

        if not re.search(r'[A-Z]', password):
            messages.error(request, 'Error: Password must contain at least one capital letter!')
            return render(request, 'register.html', {'form': register_form})

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            messages.error(request, 'Error: The password must contain at least one special character!')
            return render(request, 'register.html', {'form': register_form})

        if register_form.is_valid() and (email != '' and username != ''):
            register_form.save()
            messages.success(request, 'Your login has been successfully created!')
            return redirect('login_request')
        else:
            # messages.error(request, registerForm.error_messages)
            # messages.error(request, registerForm.errors)
            messages.error(request, 'Something went wrong, please try again!')
            return redirect('register')

    return render(request, 'register.html', {'form': register_form})


def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        # email = request.POST.get('username')
        password = request.POST['password']
        # email = request.POST.get('password')

        # user = authenticate(request, email=email, password=password)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password did not match. Please try again!')

    return render(request, 'login.html')


def logout_request(request):
    logout(request)
    messages.info(request, 'You have logged out successfully')
    return redirect('login_request')
    # return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


# from django.contrib import messages
# import re
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email


# def home(request):
#     return render(request, 'home.html')
#
#
# def registration(request):
#
#     if request.method == 'POST':
#
#         password = request.POST['password']
#         password_repeat = request.POST['password-repeat']
#
#         if password != password_repeat:
#             messages.error(request, 'Erro: Password não é igual nos dois campos!')
#             return render(request, 'registration.html')
#
#         if len(password) < 8:
#             messages.error(request, 'Erro: A password tem menos 8 caracteres!')
#             return render(request, 'registration.html')
#
#         if not re.search(r'\d', password):
#             messages.error(request, 'Erro: A password deve conter pelo menos um número!')
#             return render(request, 'registration.html')
#
#         if not re.search(r'[A-Z]', password):
#             messages.error(request, 'Erro: A password deve conter pelo menos uma letra maiúscula!')
#             return render(request, 'registration.html')
#
#         if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
#             messages.error(request, 'Erro: A password deve conter pelo menos um caractere especial!')
#             return render(request, 'registration.html')
#
#         try:
#             validate_email(request.POST['email'])
#             messages.success(request, 'Boa!')
#         except ValidationError:
#             messages.error(request, 'Erro: Endereço de email inválido!')
#         return render(request, 'registration.html')
#
#     return render(request, 'registration.html')
