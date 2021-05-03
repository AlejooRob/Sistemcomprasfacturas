from django.shortcuts import render
from django.views import generic

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from datetime import datetime

from bases.views import SinPrivilegios, VistaBaseCreate, VistaBaseEdit
from .models import Cliente, FacturaDet, FacturaEnc
from .forms import ClienteForm
import inv.views as inv 

class ClienteView(SinPrivilegios, generic.ListView):
    model = Cliente
    template_name = 'fac/cliente_list.html'
    context_object_name = 'obj'
    permission_required = 'fac.view_cliente'



class ClienteNew(VistaBaseCreate):
    model=Cliente
    template_name='fac/cliente_form.html'
    form_class=ClienteForm
    success_url=reverse_lazy('fac:cliente_list')
    permission_required='fac.add_cliente'

class ClienteEdit(VistaBaseEdit):
    model=Cliente
    template_name='fac/cliente_form.html'
    form_class=ClienteForm
    success_url=reverse_lazy('fac:cliente_list')
    permission_required='fac.change_cliente'

@login_required(login_url='/login/')
@permission_required('fac.change_cliente', login_url='/login/')
def clienteInactivar(request, id):
    cliente = Cliente.objects.filter(pk=id).first()

    if request.method=='POST':
        if cliente:
            cliente.estado = not cliente.estado
            cliente.save()
            return HttpResponse('OK')
        return HttpResponse('FAIL')
    
    return HttpResponse('FAIL')

class FacturaView(SinPrivilegios, generic.ListView):
    model=FacturaEnc
    template_name = 'fac/factura_list.html'
    context_object_name = 'obj'
    permission_required = 'fac.view_facturaenc'

@login_required(login_url='/login/')
@permission_required('fac.change_facturasenc', login_url='bases:sin_privilegios')
def facturas(request,id=None):
    template_name = 'fac/facturas.html'
    encabezado = {
        'fecha':datetime.today()
    }
    detalle={}
    clientes = Cliente.objects.filter(estado=True)
    contexto = {"enc":encabezado, "det":detalle, "clientes":clientes}


    return render(request, template_name, contexto)

class ProductoView(inv.ProductoView):
    template_name='fac/buscar_producto.html'