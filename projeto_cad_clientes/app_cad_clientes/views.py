from django.shortcuts import render
from .models import Cliente

def home(request):
    return render(request,'clientes/home.html')

def clientes(request):
    #Salvar dados da tela para o banco de dados
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get('nome')
    novo_cliente.endereco = request.POST.get('endereco')
    novo_cliente.aparelho = request.POST.get('aparelho')
    novo_cliente.problema = request.POST.get('problema')
    novo_cliente.valor_pecas = request.POST.get('valor_pecas')
    novo_cliente.mao_de_obra = request.POST.get('mao_de_obra')
    novo_cliente.total_servico = request.POST.get('total_servico')
    novo_cliente.pediu_nota = request.POST.get('pediu_nota')
    novo_cliente.save()
    # exibir todos os usuários já cadastrados em uma nova página
    clientes = {
        'clientes': Cliente.objects.all()
    }
    # Retornar os dados para a página de listagem de usuários
    return render(request,'clientes/clientes.html',clientes)