# View de perfil de usuário
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	return render(request, 'usuarios/profile.html')
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.set_password(form.cleaned_data['password'])
			user.save()
			login(request, user)
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'usuarios/register.html', {'form': form})

# As views de autenticação padrão do Django já estão disponíveis via django.contrib.auth.urls
# Para reset de senha, confirmação por email, etc, utilize as views padrão ou crie customizações aqui.
