from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Tarefa
from .forms import TarefaForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

@login_required
def lista_tarefas(request):
    # Exibe apenas tarefas do usuário logado
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'tarefas/lista_tarefas.html', {'tarefas': tarefas})

@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso.')
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

@login_required
def editar_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'tarefas/editar_tarefa.html', {'form': form})

@login_required
def excluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.delete()
    messages.success(request, 'Tarefa excluída com sucesso.')
    return redirect('lista_tarefas')

@login_required
def concluir_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, usuario=request.user)
    tarefa.concluida = True
    tarefa.save()
    return redirect('lista_tarefas')