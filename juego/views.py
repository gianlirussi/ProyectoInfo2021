# Create your views here.
from django.shortcuts import render, redirect
from .models import Pregunta, Respuesta, Partida
from datetime import datetime

from django.contrib.auth.decorators import login_required
from .models import Categoria
# Create your views here.
@login_required(login_url='/login')
def listar_preguntas(request):
    if request.method == "POST":
        resultado = 0
        for i in range(1, 10):
            opcion = Respuesta.objects.get(pk=request.POST[str(i)])
            resultado += opcion.puntaje
        Partida.objects.create(usuario=request.user, fecha=datetime.now, resultado=resultado)
        return redirect("/juego/partidas")
    else:
        data = {}
        preguntas = Pregunta.objects.all().order_by('?')[:10]
        for item in preguntas:
            respuestas = Respuesta.objects.filter(id_pregunta= item.id)
            categoria = Categoria.objects.get(pk=item.id_categoria.id)
            #{pregunta: {opciones: [opcion1, opcion2, opcionn], categoria: categoria}
            data[item.pregunta]= {'opciones': respuestas, 'categoria': categoria}
        return render(request, 'juego/listar_preguntas.html', {"preguntas": preguntas, "data": data})


@login_required(login_url='/login')
def crear_pregunta(request):
    form = PreguntaForm()
    return render(request, 'juego/crear_pregunta.html', {'form': form})

from django.contrib.auth.decorators import permission_required
@login_required(login_url='/login')
@permission_required('juedo.views_pregunta', login_url='/login')
def preguntas(request):
    preguntas= Pregunta.objects.all()
    return render(request, 'juego/preguntas.html', {"preguntas": preguntas})

@permission_required('juedo.views_pregunta', login_url='/login')
@login_required(login_url='/login')
def detalle_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juego/detalle_pregunta.html', {"pregunta": pregunta})

from .forms import PreguntaForm
from django.contrib.auth.decorators import permission_required

@login_required(login_url='/login')
@permission_required('juedo.add_pregunta', login_url='/login')
def crear_pregunta(request):
    form = PreguntaForm()
    if request.method == "POST":
        form = PreguntaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
            return redirect('juego:preguntas')
    return render(request, 'juego/crear_pregunta.html', {'form': form})

@permission_required('juedo.change_pregunta', login_url='/login')
@login_required(login_url='/login')
def editar_pregunta(request, identificador):
    pregunta= Pregunta.objects.get(pk=identificador)
    if request.method == "POST":
        form = PreguntaForm(request.POST, instance=pregunta)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.fecha_creacion = datetime.now()
            item.save()
            return redirect('juego:detalle_pregunta', identificador=item.id)
    else:
        form = PreguntaForm(instance=pregunta)
    return render(request, 'juego/editar_pregunta.html', {'form': form})

@permission_required('juedo.delete_pregunta', login_url='/login')
@login_required(login_url='/login')
def eliminar_pregunta(request, identificador):
    pregunta = Pregunta.objects.get(pk=identificador)
    return render(request, 'juego/eliminar_pregunta.html', {"pregunta": pregunta})


@login_required(login_url='/login')
def confirmar_eliminacion(request, identificador):
    Pregunta.objects.get(pk=identificador).delete()
    return redirect("juego:preguntas")

@permission_required('juedo.add_respuesta', login_url='/login')
@login_required(login_url='/login')
def crear_respuesta(request):
    form = RespuestaForm()
    return render(request, 'juego/crear_respuesta.html', {'form': form})

from django.contrib.auth.decorators import permission_required
@login_required(login_url='/login')
@permission_required('juedo.views_respuestas', login_url='/login')
def respuestas(request):
    respuestas= Respuesta.objects.all()
    return render(request, 'juego/respuestas.html', {"respuestas": respuestas})

from django.contrib.auth.decorators import permission_required
@permission_required('juedo.views_respuestas', login_url='/login')
@login_required(login_url='/login')
def detalle_respuesta(request, identificador):
    respuesta = Respuesta.objects.get(pk=identificador)
    return render(request, 'juego/detalle_respuesta.html', {"respuesta": respuesta})

from .forms import RespuestaForm
from django.contrib.auth.decorators import permission_required

@login_required(login_url='/login')
@permission_required('juedo.add_respuesta', login_url='/login')
def crear_respuesta(request):
    form = RespuestaForm()
    if request.method == "POST":
        form = RespuestaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
            return redirect('juego:respuestas')
    return render(request, 'juego/crear_respuesta.html', {'form': form})

@permission_required('juedo.change_respuesta', login_url='/login')
@login_required(login_url='/login')
def editar_respuesta(request, identificador):
    respuesta= Respuesta.objects.get(pk=identificador)
    if request.method == "POST":
        form = RespuestaForm(request.POST, instance=respuesta)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.fecha_creacion = datetime.now()
            item.save()
            return redirect('juego:detalle_respuesta', identificador=item.id)
    else:
        form = RespuestaForm(instance=respuesta)
    return render(request, 'juego/editar_respuesta.html', {'form': form})

@permission_required('juedo.delete_respuesta', login_url='/login')
@login_required(login_url='/login')
def eliminar_respuesta(request, identificador):
    respuesta = Respuesta.objects.get(pk=identificador)
    return render(request, 'juego/eliminar_respuesta.html', {"respuesta": respuesta})


@login_required(login_url='/login')
def confirmar_eliminacionn(request, identificador):
    Respuesta.objects.get(pk=identificador).delete()
    return redirect("juego:respuestas")

@permission_required('juedo.add_categoria', login_url='/login')
@login_required(login_url='/login')
def crear_categoria(request):
    form = CategoriaForm()
    return render(request, 'juego/crear_categoria.html', {'form': form})

from django.contrib.auth.decorators import permission_required
@login_required(login_url='/login')
@permission_required('juedo.views_categoria', login_url='/login')
def categorias(request):
    categorias= Categoria.objects.all()
    return render(request, 'juego/categorias.html', {"categorias": categorias})

from django.contrib.auth.decorators import permission_required
@permission_required('juedo.views_categoria', login_url='/login')
@login_required(login_url='/login')
def detalle_categoria(request, identificador):
    categoria = Categoria.objects.get(pk=identificador)
    return render(request, 'juego/detalle_categoria.html', {"categoria": categoria})

from .forms import CategoriaForm
from django.contrib.auth.decorators import permission_required

@login_required(login_url='/login')
@permission_required('juedo.add_categoria', login_url='/login')
def crear_categoria(request):
    form = CategoriaForm()
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.autor = request.user
            registro.fecha_creacion = datetime.now()
            registro.save()
            return redirect('juego:categoria')
    return render(request, 'juego/crear_categoria.html', {'form': form})

@permission_required('juedo.change_categoria', login_url='/login')
@login_required(login_url='/login')
def editar_categoria(request, identificador):
    categoria= Categoria.objects.get(pk=identificador)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=respuesta)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.fecha_creacion = datetime.now()
            item.save()
            return redirect('juego:detalle_categoria', identificador=item.id)
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'juego/editar_categoria.html', {'form': form})

@permission_required('juedo.delete_categoria', login_url='/login')
@login_required(login_url='/login')
def eliminar_categoria(request, identificador):
    categoria = Categoria.objects.get(pk=identificador)
    return render(request, 'juego/eliminar_categoria.html', {"categoria": categoria})


@login_required(login_url='/login')
def confirmar_eliminaciion(request, identificador):
    Categoria.objects.get(pk=identificador).delete()
    return redirect("juego:categoria")

def pagina(request):
    return render(request, 'juego/pagina.html')

def noticias(request):
    return render(request, "juego/noticias.html")

@login_required(login_url='/login')
def partidas(request):
    partidas = Partida.objects.all().order_by('-fecha')[:5]
    return render(request, "juego/partidas.html", {"partidas": partidas})


