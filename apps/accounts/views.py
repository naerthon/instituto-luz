from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm

@permission_required('is_superuser')
def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            # login(request, user)
            return redirect('core:index')
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)