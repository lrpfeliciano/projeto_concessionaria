
from django.shortcuts import render, redirect
from cadastro.forms import MarcaForm

from cadastro.models import Cliente, Marca

# Create your views here.

def listarMarcas(request):
    marcas = Marca.objects.order_by('nome') 
    return render(request, 'marcas/lista.html', {'marcas': marcas} )

def incluirMarca(request):
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    form = MarcaForm()
    return render(request, 'marcas/form_marca.html',
        {'form': form})

def alterarMarca(request, id):
    marca = Marca.objects.get(id = id)

    if request.method == "POST":
        form = MarcaForm(request.POST, instance = marca)
        if form.is_valid():
            form.save()
            return redirect('listar_marcas')
    form = MarcaForm(instance = marca)
    return render(request, 'marcas/form_marca.html',
        {'form': form})

def excluirMarca(request, id):
    marca = Marca.objects.get(id = id)        
    try:
        marca.delete()
    except:
        pass
    return redirect("listar_marcas")

def listarClientes(request):
    clientes = Cliente.objects.order_by('nome')
    return render(request, 'clientes/lista.html', 
        {'clientes': clientes} )

def index(request):
    return render(request, 'index.html')

def segundo(request):
    return render(request, 'pagina2.html')
