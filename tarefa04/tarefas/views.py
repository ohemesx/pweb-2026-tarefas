from django.shortcuts import render
from datetime import date
from .models import Tarefa
# Create your views here.
def lista_tarefas(request):
    hoje = date.today()
    tarefas = Tarefa.objects.all()
    context = {
        'tarefas': tarefas,
        'hoje': hoje
    }
    return render(request, 'tarefas/lista_tarefas.html', context)
