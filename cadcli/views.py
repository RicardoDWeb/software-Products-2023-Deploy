from . models import Cliente
from . forms import ClienteForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import transaction
from django.db import connection
from django.core.paginator import Paginator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def pagina_inicial(request):
    return render(request, 'cadcli/pagina_inicial.html')

def pagina_de_sucesso(request):
    return render(request, 'cadcli/formulario_sucesso_incluir.html')

def pagina_exclusao_sucesso(request):
    return render(request, 'cadcli/formulario_sucesso_delete.html')

def cadastrar_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')

    try:

        # Instância do modelo Cliente, salvando no banco de dados
        cliente = Cliente.objects.create(nome_cliente=nome, email_cliente=email, tel_cliente=telefone)
        return HttpResponseRedirect('cadcli:pagina_de_sucesso')  # Redirecionar para a página de sucesso

    except Exception as e:
        # Lidar com exceções, por exemplo, exibir uma mensagem de erro
        return render(request, 'cadcli/formulario_incluir.html', {'error_message': str(e)})
    #
    # else:
    #
    #    return render(request, 'cadcli/formulario_incluir.html')


def consultar_todos_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'cadcli/consultar_todos_clientes.html', {'clientes':clientes})

def alterar_cliente(request):
    # Obtém todos os clientes da base de dados
    clientes = Cliente.objects.all()

    return render(request, 'cadcli/alterar_cliente.html', {'clientes': clientes})

def alterar_um_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cadcli:alterar_cliente')  # Redirecione de volta para a lista de clientes após a edição.
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'cadcli/alterar_um_cliente.html', {'form': form, 'cliente': cliente})

def excluir_cliente(request):
    # Obtém todos os clientes da base de dados
    clientes = Cliente.objects.all()

    return render(request, 'cadcli/excluir_cliente.html', {'clientes': clientes})

def excluir_um_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        cliente.delete()
        return redirect('cadcli:excluir_cliente')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'cadcli/excluir_um_cliente.html', {'form': form, 'cliente': cliente})