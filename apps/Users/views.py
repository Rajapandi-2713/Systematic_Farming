from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, EmailForm, OTPForm,PasswordForm
from .models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.utils import timezone


# Customized Login View - /auth/login
def Loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password, backend='apps.Users.backends.EmailBackend')
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form_error = {"error":'Invalid email or password. Please try again.'}
                return render(request, 'users/login.html', {'form': form ,'form_error':form_error})
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form })


# Register - /auth/register
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend='apps.Users.backends.EmailBackend'
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Log the user in after registration
            login(request, user)
            return redirect('home')
             # Redirect to the home page after successful registration

        else :

            # Error message handling
            form_error = {}
            for field, errors in form.errors.items():
                error_list =[]
                for error in errors:
                    error_list.append(error)
                form_error[field] = error_list

            # {'password': ['Password must be at least 4 characters long.']}
            return render(request, 'users/register.html', {'form': form,'form_error': form_error})
           
    else:
        form = RegistrationForm()

    return render(request, 'users/register.html', {'form': form})


# register page - /auth/forgot-password
def forgot_password(request):
    if request.method == 'POST':
        email_form = EmailForm(request.POST)
        print('Post method executed')
        if email_form.is_valid():
            email = email_form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                print('User found',user)
            except User.DoesNotExist:
                print('User not found')
                form_error = {"error":'No user associcated with this email !'}
                form = EmailForm()
                return render(request, 'users/forgot_password.html', {'form': form ,'form_error':form_error})

            # Generate and save OTP
            otp = get_random_string(length=6, allowed_chars='0123456789')
            user.otp = otp
            user.otp_expire = (timezone.now() + timezone.timedelta(minutes=5)) # OTP expires in 5 minutes
            user.save()
            print(otp)
            print('otp generated and saved')

            # Send OTP to the user via email
            print('ready to send')
            send_mail(
                'Password Reset OTP',
                f'Your OTP for password reset is: {otp}',
                'noreply@agriplanet.com',
                [email],
                fail_silently=False,
            )
            print('send successfully')

            return redirect('otp-validation')
    else:
        email_form = EmailForm()

    return render(request, 'users/forgot_password.html', {'form': email_form})


# Otp validation - /auth/otp-validation
def otp_validation(request):
    if request.method == 'POST':
        otp_form = OTPForm(request.POST)
        if otp_form.is_valid():
            otp = otp_form.cleaned_data['otp']
            user = User.objects.filter(otp=otp).first()
            user.backend='apps.Users.backends.EmailBackend'
            if user:
                login(request,user)
                return redirect('password-reset')
            else:
                form_error = {"error":' Invalid OTP !'}
                form = OTPForm()
                return render(request, 'users/otp.html', {'form': form ,'form_error':form_error})

    else:
        otp_form = OTPForm()

    return render(request, 'users/otp.html', {'form': otp_form})


# Password Reset - /auth/password-reset
def password_reset(request):
    if request.method == 'POST':
        password_form = PasswordForm(request.POST)
        if password_form.is_valid():
            password = password_form.cleaned_data['password']
            user = User.objects.get(email = request.user.email)
            user.backend='apps.Users.backends.EmailBackend'
            if user and user.otp_expire > timezone.now():
                user.set_password(password) 
                user.otp = None
                user.otp_expire = None
                user.save()
                return redirect('home')
        else:
            form_error = {"error": 'Password must be at least 4 characters long.!'}
            form = PasswordForm()
            return render(request, 'users/password_reset.html', {'form': form ,'form_error':form_error})

    else:
        password_form = PasswordForm()
        return render(request,'users/password_reset.html',{'form':password_form})


# Testing home page - /auth/home
@login_required
def home(request):
    return render(request, 'index.html')