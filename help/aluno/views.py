from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Aluno
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def lista_alunos(request): # Funcao que renderiza a lista de alunos dado uma pesquisa por nome ou nao
    alunos = Aluno.objects.order_by('nome')
    query = request.GET.get("q")
    if query:
        alunos = alunos.filter(nome__icontains=query)
    return render(request, 'aluno/lista_alunos.html', {'alunos':alunos})

@login_required
def detalhes(request, pk): # Funcao que exibe os detalhes de aluno para edicao ou remocao
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno/detalhes.html', {'aluno': aluno})

@login_required
def novo(request): # Funcao para criar um novo aluno
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            now = datetime.now();
            post = form.save(commit=False)
            post.data_entrada = timezone.now()
            post.numero_matricula = datetime.now().strftime("%y%m%d") + post.cpf[7:11];
            post.save()
            return redirect('aluno:detalhes', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'aluno/novo.html', {'form': form})

@login_required
def editar(request, pk): # Funcao para editar um aluno
    post = get_object_or_404(Aluno, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('aluno:detalhes', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'aluno/novo.html', {'form': form})

@login_required
def remover(request, pk): # Funcao para remover um aluno
    aluno = Aluno.objects.filter(pk=pk)
    aluno.delete()
    return render(request,'aluno/confirmacao.html')