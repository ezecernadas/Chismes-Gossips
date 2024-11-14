from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from pagina.models import Agenda, Usuarios, Publicaciones
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from pagina.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.session.has_key('userId'):    
        return redirect(panel)
    else:
        return render(request, './index.html')

def contacto(request):
    try:
        mis_contactos = Agenda.objects.all()
        print(mis_contactos)
    except Exception:
        print(Exception)
    return render(request, './contacto.html',
                  {'profesor': "Fedegoo",
                   'contacto':mis_contactos})

def crearContacto(request):
    if request.method== 'POST':
        print('se ejecuto el post')
        nombre = request.POST['name']
        apellido = request.POST['surname']
        dni = request.POST['dni']
        agenda= Agenda(nombre = nombre,
                       apellido=apellido,
                       dni=dni)
        agenda.save()
        return redirect('home')
    return render(request, './crearContacto.html')

def instaMenu(request):
    return render(request, './instaMenu.html')

def loginPage(request):

    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request,user)
            return redirect('panel')
        else:
            messages.warning(request, 'No se pudo iniciar sesion')
            return render(request, './registration/login.html')
    
    return render(request, './registration/login.html'   )

def register(request):
    register_form=RegisterForm(request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te registraste con exito')
            return redirect ('login')
        print('capo')
    return render(request,'./registration/register.html', {'register_form':register_form}) 

@login_required
def panel(request):
    publicaciones = Publicaciones.objects.all().order_by('-fechaCreacion')
    usuarios = User.objects.all()
    return render(request, './panel.html', {"comentarios": publicaciones, "usuarios":usuarios , "idUsuario": request.user.id})

def agregarPosteo(request):
    publicaciones = Publicaciones(
        idUsuario= request.user.id,
        contenido= request.POST['contenidoPosteo'],
        likes = 0,
        dislike = 0
    )
    publicaciones.save()
    return redirect('panel')
    
def logoutPage(request):
    logout(request)
    return redirect('home')

def editPost(request, id):
    posteo = Publicaciones.objects.get(pk=id)
    posteo.contenido = request.POST['contenidoPosteo']
    posteo.save()
    return redirect('miPerfil')

def deletePost(request, id):
    publicaciones = Publicaciones.objects.get(pk=id)
    publicaciones.delete()
    return redirect('miPerfil')

def deleteContacto(request, id):
    agenda = Agenda.objects.get(pk=id)
    agenda.delete()
    return redirect('contacto')

@login_required
def miPerfil(request):
    publicaciones = Publicaciones.objects.all().order_by('-fechaCreacion')
    cont = 0
    for posteo in publicaciones:
        if posteo.idUsuario == request.user.id:
            cont = cont + 1
    if request.method == 'POST': 
        idPost = request.POST['editButton']
        return render(request, './miPerfil.html',{"idUsuario": request.user.id, "user":request.user.username,"email":request.user.email,"nombre":request.user.last_name,"apellido":request.user.first_name,"comentarios": publicaciones,"cantComentarios":cont,"editMenu":idPost})

    return render(request, './miPerfil.html',{"idUsuario": request.user.id, "user":request.user.username,"email":request.user.email,"nombre":request.user.last_name,"apellido":request.user.first_name,"comentarios": publicaciones,"cantComentarios":cont})