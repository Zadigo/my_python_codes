from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View

from django.http import request, HttpResponseRedirect

from django.core.mail import send_mail, BadHeaderError

from django.conf import settings

from django.contrib.auth.decorators import login_required, user_passes_test

from django.db.models import Q

# from courses.models import FamilyCourse, TeacherApplication

from accounts.models import MyUserProfile

from accounts.forms import MyUserTeacherProfileForm, MyUserLearnerProfileForm, UserLoginForm, UserCreationForm
from accounts.forms import UserLoginForm, UserForgotPasswordForm, UserSignupForm

from django.contrib import messages
from django.contrib.messages import add_message


MyUser = get_user_model()

# Registrations

def signup_user(request):
    context={'form':UserSignupForm}
    template_name='registration/signup.html'

    if request.method == 'POST':
        nom         = request.POST['nom']
        prenom      = request.POST['prenom']
        email       = request.POST['email']
        password    = request.POST['password']

        if MyUser.objects.filter(email__iexact=email).exists():
            add_message(request, messages.WARNING, 'Il semblerait que vous ayez déjà un compte chez nous', extra_tags='warning')
        else:
            user = MyUser.objects.create_user(email, nom=nom, prenom=prenom, password=password)

            if user:
                return redirect('/login/', permanent=False)

    return render(request, template_name, context)

def login_user(request):
    context={'form': UserLoginForm}
    template_name   = 'registration/login.html'

    if request.method == 'POST':
        email       = request.POST['email']
        password    = request.POST['password']
        user        = authenticate(request, email=email, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next') or 'profile')

        else:
            add_message(request, messages.INFO, 'Votre adresse mail ou mot de passe ne sont pas correctes', extra_tags='warning')

    return render(request, template_name, context)

def logout_user(request):
    add_message(request, messages.INFO, 'Vous avez été déconnecté', extra_tags='success')
    return redirect('/login/', permanent=False)

def forgot_password(request):
    context = {'form': UserForgotPasswordForm}
    template_name = 'registration/forgot_password.html'

    if request.method == 'POST':
        email = request.POST['email']

        user = MyUser.objects.get(email=email)

        if user:
            try:
                send_mail(
                    'Restauration',
                    'Veuillez suivre ce lien pour ...',
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
            except BadHeaderError:
                add_message(request, messages.WARNING, 'Une erreur c\'est produite', extra_tags='warning')
                template_name = 'registration/forgot.html'
            else:
                add_message(request, messages.INFO, 'Veuillez consulter votre boite mail', extra_tags='warning')
                template_name = 'registration/login.html'
        
        else:
            add_message(request, messages.WARNING, 'Nous n\'avons pas réussi à vous trouver dans notre base de données')
            template_name = 'registration/forgot-password.html'

    return render(request, template_name, context)

def change_password(request):
    # TODO
    context = {'form':UserChangePasswordForm}
    template_name = 'registration/change_password.html'
    form = UserChangePasswordForm(request.POST)
    if form.is_valid():
        add_message(request, messages.INFO, 'Votre mot de passe a été changé', extra_tags='success')
        return redirect('/login/', permanent=False)
    return render(request, template_name, context)

# Profile

class ProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.is_admin:
            return redirect('/admin/', permanent=False)
        
        return render(request, 'accounts/profile.html')

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pass
        
        return render(request, 'accounts/profile_edit.html', {})

    def post(self, request, *args, **kwargs):
        pass


# Other

def accounts_redirection(request):
    if request.user.is_authenticated:
        template_name = '/profile/'
    else:
        template_name = '/signup/'

    return redirect(template_name, permanent=False)

