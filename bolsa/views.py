from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)  
from .models import PerfilUsuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseRedirect
from .forms import (
    ContactFormForm,
    UserUpdateForm,
    PerfilUpdateForm,AccionForm
)

from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth import login
from datetime import datetime
# from .forms import RegistroUser

# buscador
from django.http import JsonResponse
from .models import (
PerfilUsuario,Accion,Transaccion, Tipo_trx
)
from django.http import JsonResponse

from django.db.models import Sum


# Create your views here.
def indice(request):
    context= {}
    if request.user.is_authenticated:
        #perfil = PerfilUsuario.objects.get(user=request.user)


        # Guarda el username y el id del tipo de usuario en la sesión
        request.session["usuario"] = request.user.username
        #request.session["tipousuario"] = request.user.username
        # Verifica si hay un registro en la tabla PerfilUsuario para el usuario
        existe_perfil = PerfilUsuario.objects.filter(user=request.user).exists()

        # Asigna el tipo de usuario según la existencia del perfil
        if existe_perfil:
            request.session["tipousuario"] = "regular"
        else:
            request.session["tipousuario"] = "admin"
                    
        context= {"usuario": request.session["usuario"],"tipousuario": request.session["tipousuario"]}
        return render(request,"index.html", context, )

        #request.session["tipo_usuario"] = perfil.tipo.id 
        # Recupera los valores almacenados para enviarlos al template
        #print(request.session["tipo_usuario"])
        #if request.session["tipo_usuario"] == 3:
        #    context = {
        #        "usuario": request.session["usuario"],
        #        "tipo_usuario": request.session["tipo_usuario"],
        #    }
        #elif request.session["tipo_usuario"] == 1:
        #    # Obtener al relator según el id de usuario
        #    print(perfil.id)
        #    relator = Usuario.objects.get(id=perfil.id)  # Usamos el ID del usuario para obtener al relator
            
        #    # Obtener los cursos asignados a este relator
        #    cursos = Curso.objects.filter(relator_id=relator)#.select_related('idcurso')

        #    # Pasar los cursos y el usuario al contexto
        #    context = {
        #        "usuario": request.session["usuario"],
        #        "tipo_usuario": request.session["tipo_usuario"],
        #        "cursos": cursos,
        #    } 
        #    return render(
        #    request,
        #    "index.html",
        #    context,
        #   )

        #elif request.session["tipo_usuario"] == 4:
        #    alumno = Usuario.objects.get(id=perfil.id)  # Usamos el ID del usuario para obtener al alumno
            
        #    # Obtener los cursos a los que está inscrito este alumno
        #    cursos_alumno = AlumnosCurso.objects.filter(idusuario=alumno)
            
        #    # Obtener los cursos completos relacionados a estos registros de AlumnosCurso
        #    cursos = [cursos_alumno_item.idcurso for cursos_alumno_item in cursos_alumno]

        #    # Pasar los cursos y el usuario al contexto
        #    context = {
        #        "usuario": request.session["usuario"],
        #        "tipo_usuario": request.session["tipo_usuario"],
        #        "cursos": cursos,
        #    }
        #    return render(
        #    request,
        #    "index.html",
        #    context,
        #   )

    return render(request, "index.html")

    #return render(request, "index.html")

def register(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("indice")
        else:
            print("Errores:", form.errors)
    else:
        form = RegistroForm()
    return render(
        request, template_name="registration/register.html", context={"form": form}
    )


# editar un usuario
@login_required
# actualizar datos del perfil
def misdatos(request):
    perfil = PerfilUsuario.objects.get(user=request.user)
    # se envia por parametro los 2 modelos
    context = {
        "user": request.user,  # Datos del user de django
        "perfil": perfil,  # Datos perfilusuario
        # ,'tipo_usuario': tipousuario
    }
    return render(request, "misdatos.html", context)


@login_required
def update_profile(request):
    # Obtener o crear el perfil del usuario si no existe
    perfil, created = PerfilUsuario.objects.get_or_create(user=request.user)

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        perfil_form = PerfilUpdateForm(request.POST, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "Tu perfil ha sido actualizado.")
            return redirect("misdatos")
            # return redirect("update_profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        perfil_form = PerfilUpdateForm(instance=perfil)

    context = {"user_form": user_form, "perfil_form": perfil_form}
    return render(request, "update_profile.html", context)



#Acciones
@login_required

def accion_list(request):
    accion = Accion.objects.all()  # Obtén todos los cursos
    return render(request, "acciones_list.html", {"accion": accion})

# Vista para crear un acciones
@login_required
def create_acciones(request):
    if request.method == "POST":
        form = AccionForm(request.POST)
        if form.is_valid():
            accion = form.save(commit=False)  
             
            accion.save()  
            messages.success(request, "Accion ha sido creado.")
            return redirect("accion_list")  # Redirige a la lista de cursos
    else:
        form = AccionForm()
    return render(request, "acciones_form.html", {"form": form})

# Vista para editar un acciones
@login_required
def edit_acciones(request, accion_id):
    curso = get_object_or_404(Accion, pk=accion_id)
    if request.method == "POST":
        form = AccionForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect("accion_list")  # Redirige a la lista de cursos
    else:
        form = AccionForm(instance=curso)
    return render(request, "acciones_form.html", {"form": form, "curso": curso})

# Vista para eliminar un acciones
@login_required
def delete_acciones(request, accion_id):
    accion = get_object_or_404(Accion, pk=accion_id)
    accion.delete()  # Elimina el curso
    return redirect("accion_list")


#regular
@login_required
def listar_acciones(request):
    acciones = Accion.objects.all()
    perfil = get_object_or_404(PerfilUsuario, user=request.user)
    return render(request, "regular/listar_acciones.html", {"acciones": acciones, "perfil": perfil})

@login_required
def comprar_accion(request, accion_id):
    accion = get_object_or_404(Accion, id=accion_id)
    perfil = get_object_or_404(PerfilUsuario, user=request.user)

    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 0))
        costo_total = accion.precio_actual * cantidad

        if cantidad <= 0:
            messages.error(request, "La cantidad debe ser mayor a cero.")
            return redirect("comprar_accion", accion_id=accion.id)

        if perfil.saldo < costo_total:
            messages.error(request, "No tienes saldo suficiente para realizar esta compra.")
            return redirect("comprar_accion", accion_id=accion.id)

        # Actualizar saldo del usuario
        perfil.saldo -= costo_total
        perfil.save()

        # Registrar la transacción
        tipo_compra = Tipo_trx.objects.get(id_tipo=1)  # Asume que el ID 1 corresponde a compra
        transaccion = Transaccion.objects.create(
            usuario_id=request.user,
            accion_id=accion,
            tipo_transaccion="Compra",
            cantidad=cantidad,
            Precio=costo_total,
            tipotrx=tipo_compra,
            fecha_transaccion=datetime.now(),
        )
        transaccion.save()

        messages.success(request, f"Has comprado {cantidad} acciones de {accion.nombre_empresa}.")
        return redirect("listar_acciones")  # Redirige a la lista de acciones después de la compra

    return render(request, "regular/comprar_accion.html", {"accion": accion, "perfil": perfil})


@login_required
def vender_accion(request, accion_id):
    if not request.user.is_authenticated:
        messages.error(request, "Debes iniciar sesión para realizar esta acción.")
        return redirect("login")

    accion = get_object_or_404(Accion, id=accion_id)

    # Calcular el total de acciones compradas por el usuario para esta acción
    total_compradas = Transaccion.objects.filter(
        usuario_id=request.user,
        accion_id=accion,
        tipo_transaccion="compra"
    ).aggregate(total=Sum("cantidad"))["total"] or 0

    # Calcular el total de acciones vendidas por el usuario para esta acción
    total_vendidas = Transaccion.objects.filter(
        usuario_id=request.user,
        accion_id=accion,
        tipo_transaccion="venta"
    ).aggregate(total=Sum("cantidad"))["total"] or 0

    # Acciones disponibles para vender
    disponibles = total_compradas - total_vendidas

    if request.method == "POST":
        cantidad_a_vender = int(request.POST.get("cantidad"))

        # Validar que el usuario tiene suficientes acciones para vender
        if cantidad_a_vender > disponibles:
            messages.error(request, "No tienes suficientes acciones para vender.")
            return redirect("vender_accion", accion_id=accion.id)

        # Registrar la venta como una transacción
        Transaccion.objects.create(
            usuario_id=request.user,
            accion_id=accion,
            tipo_transaccion="venta",
            cantidad=cantidad_a_vender,
            Precio=accion.precio_actual,
            tipotrx_id=2  # Supongamos que el tipo 2 es "venta"
        )

        messages.success(request, f"Has vendido {cantidad_a_vender} acciones de {accion.nombre_empresa}.")
        return redirect("historial_transacciones")

    return render(request, "regular/vender_accion.html", {
        "accion": accion,
        "disponibles": disponibles
    })

@login_required
def acciones_compradas(request):
    # Obtener las transacciones de compra del usuario
    transacciones = Transaccion.objects.filter(
        usuario_id=request.user, tipotrx=1#tipo_transaccion="Compra"
    )

    # Crear un diccionario para acumular las cantidades de acciones por empresa
    acciones_compradas = {}
    for transaccion in transacciones:
        if transaccion.accion_id not in acciones_compradas:
            acciones_compradas[transaccion.accion_id] = {
                'nombre_empresa': transaccion.accion_id.nombre_empresa,
                'cantidad': 0,
                'precio_actual': transaccion.accion_id.precio_actual,
            }
        acciones_compradas[transaccion.accion_id]['cantidad'] += transaccion.cantidad

    return render(
        request,
        "regular/acciones_compradas.html",
        {"acciones_compradas": acciones_compradas},
    )
    
    
@login_required
def historial_transacciones(request):
    # Obtener todas las transacciones del usuario
    transacciones = Transaccion.objects.filter(usuario_id=request.user).order_by('-fecha_transaccion')
    
    return render(
        request,
        "regular/historial_transacciones.html",
        {"transacciones": transacciones},
    )