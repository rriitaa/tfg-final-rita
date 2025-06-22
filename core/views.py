from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import EmailLoginForm, UserRegisterForm, EjercicioForm, ProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from .models import Ejercicio
from django.http import JsonResponse
from openai import OpenAI
import json


# Definimos el cliente de OpenAI



def openAIQuestion(request):
    data = json.loads(request.body)
    pregunta = data.get("message", "")
    prompt = armarPregunta(pregunta)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[{"role": "user", "content": prompt},]
    )
    contenido = completion.choices[0].message.content
    try:
        resultado_json = json.loads(contenido)
    except json.JSONDecodeError:
        resultado_json = {
            "titulo": "Error",
            "categoria": "error",
            "descripcion": "La respuesta no es un JSON válido."
        }
    return JsonResponse({"content": resultado_json})

def detalle_ejercicio(request, id):
    ejercicio = get_object_or_404(Ejercicio, id=id)
    return render(request, 'core/ejercicio-single.html', {'ejercicio': ejercicio})


def index(request):
    return render(request, 'core/index.html')

def categorias(request):
    return render(request, "core/categorias.html")

def categoria_fuerza(request):
    return render(request, "core/ejercicios_fuerza.html")

def categoria_cardio(request):
    return render(request, "core/ejercicios_cardio.html")

def categoria_flexibilidad(request):
    return render(request, "core/ejercicios_flexibilidad.html")

def categoria_gluteos(request):
    return render(request, "core/ejercicios_gluteos.html")

def categoria_espalda(request):
    return render(request, "core/ejercicios_espalda.html")



def ejercicios_gluteo_medio(request):
    return render(request, 'core/categoria_gluteo_medio.html')

def ejercicios_fuerza_medio(request):
    return render(request, 'core/categoria_fuerza_medio.html')

def ejercicios_espalda_medio(request):
    return render(request, 'core/categoria_espalda_medio.html')

def ejercicios_cardio_medio(request):
    return render(request, 'core/categoria_cardio_medio.html')

def ejercicios_flexibilidad_medio(request):
    return render(request, 'core/categoria_flexibilidad_medio.html')

def ejercicios_gluteo_alto(request):
    return render(request, 'core/categoria_gluteo_alto.html')

def ejercicios_fuerza_alto(request):
    return render(request, 'core/categoria_fuerza_alto.html')

def ejercicios_espalda_alto(request):
    return render(request, 'core/categoria_espalda_alto.html')

def ejercicios_cardio_alto(request):
    return render(request, 'core/categoria_cardio_alto.html')

def ejercicios_flexibilidad_alto(request):
    return render(request, 'core/categoria_flexibilidad_alto.html')

def todos_fuerza(request):
    return render(request, 'core/todos-fuerza.html')

def todos_cardio(request):
    return render(request, 'core/todos-cardio.html')

def todos_flex(request):
    return render(request, 'core/todos-flex.html')

def todos_gluteos(request):
    return render(request, 'core/todos-gluteos.html')

def todos_espalda(request):
    return render(request, 'core/todos-espalda.html')



def registrar(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada exitosamente")
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'core/signup.html', {'form': form})

def home(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para subir ejercicios.")
        return redirect('user_login')
    return render(request, "core/inicio.html")

def recuperar_contrasena(request):
    return render(request, 'core/recuperar.html')

def user_login(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = EmailLoginForm()
    return render(request, 'core/login.html', {'form': form})


def up_exercise(request):
    print("Subiendo ejercicio")
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para subir ejercicios.")
        return redirect('user_login')


    if request.method == 'POST':
        form = EjercicioForm(request.POST)
        if form.is_valid():
            ejercicio = form.save(commit=False)
            ejercicio.usuario = request.user
            ejercicio.save()
            return redirect('listar_ejercicios')
        else:
            print("Error en el formulario", form.errors)
            messages.error(request, "Error al subir el ejercicio")
            return redirect('subir-ejercicio')
    else:
        print("Es Get")
        form = EjercicioForm()
    return render(request, 'core/sube-ejers.html', {'form': form})

def list_exercises(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para listar ejercicios.")
        return redirect('user_login')

    ejercicios = Ejercicio.objects.order_by('-fecha_creacion')[:10]
    return render(request, 'core/comunidad.html', {'ejercicios': ejercicios})


def list_my_exercises(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para listar tus ejercicios.")
        return redirect('user_login')

    ejercicios = Ejercicio.objects.filter(usuario=request.user)
    return render(request, 'core/mis-publis.html', {'ejercicios': ejercicios})


def my_profile(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para ver tu perfil.")
        return redirect('user_login')

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'core/perfil.html', {'form': form})


def exercise_agent(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para utilizar la plataforma.")
        return redirect('user_login')

    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        if not user_message:
            return JsonResponse({"response": "No se recibió ningún mensaje."})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Eres un entrenador personal experto en rutinas y consejos de ejercicio físico."},
                    {"role": "user", "content": user_message}
                ]
            )

            respuesta = response.choices[0].message.content
            return JsonResponse({"response": respuesta})
        except Exception as e:
            print("Error con OpenAI:", str(e))
            return JsonResponse({"response": "Ocurrió un error al conectar con la IA. Intenta nuevamente."})
    else:
        return render(request, "core/ia-asistente.html")


def editar_ejercicio(request, id):
    ejercicio = get_object_or_404(Ejercicio, id=id)

    if request.method == 'POST':
        form = EjercicioForm(request.POST, instance=ejercicio)
        if form.is_valid():
            form.save()
            messages.success(request, "Ejercicio actualizado exitosamente")
            return redirect('listar_ejercicios')
        else:
            messages.error(request, "Error al actualizar el ejercicio")
    else:
        form = EjercicioForm(instance=ejercicio)

    return render(request, 'core/editar-ejercicio.html', {'form': form, 'ejercicio': ejercicio})


def eliminar_ejercicio(request, id):
    ejercicio = get_object_or_404(Ejercicio, id=id)

    if request.method == 'POST':
        ejercicio.delete()
        messages.success(request, "Ejercicio eliminado exitosamente")
        return redirect('listar_ejercicios')

    return render(request, 'core/eliminar-ejercicio.html', {'ejercicio': ejercicio})

def comienza_entreno(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Debes iniciar sesión para subir ejercicios.")
        return redirect('user_login')
    return render(request, "core/comienza-entreno.html")



#Hacer que la IA aprenda de los ejercicios que suban los usuarios:
def ejercicios_por_categoria(request, categoria):
    # Buscar hasta 5 ejercicios por categoría
    ejercicios_similares = Ejercicio.objects.filter(categoria=categoria).order_by('-fecha_creacion')[:5]
    
    # Crear el texto para mostrar
    texto_ejercicios = ""
    for ej in ejercicios_similares:
        texto_ejercicios += f"- {ej.titulo}: {ej.descripcion[:100]}...\n"

    # Puedes pasar este texto o devolverlo, pero en mi caso lo tengo con el prompt específico
    return render(request, 'ejercicios/categoria.html', {'texto_ejercicios': texto_ejercicios})





def logout_view(request):
    logout(request)
    return redirect('user_login')

def armarPregunta(pregunta_usuario):
    pregunta = f"""
    {pregunta_usuario} y devuélvelo EXCLUSIVAMENTE en formato JSON con esta estructura:
    {{
        "titulo": "...",
        "categoria": "...",
        "descripcion": "..."
    }}

    Condiciones:
    - "titulo" debe tener un máximo de 40 caracteres.
    - "categoria" debe ser UNA SOLA palabra elegida de esta lista exacta: ["fuerza", "cardio", "flexibilidad", "gluteos", "espalda"].
    - "descripcion" debe ser clara y detallada, con un máximo de 450 caracteres, y debe contener:
    - Una sección de qué músculos se trabajan,
    - Una sección de cómo se ejecuta el ejercicio paso a paso,
    - Y una sección final que indique el nivel de dificultad (básico, medio o avanzado) seguido de un consejo técnico útil comenzando con “CONSEJO:”.

    - La descripción debe estar organizada en bullet points (usando guiones o asteriscos), por ejemplo:
    - Músculos trabajados: ...
    - Ejecución: ...
    - Nivel: ...
    - Consejo: ...
    - Asegúrate de que sea un JSON *válido*.
    - Usa punto y coma (;) para separar los datos en el texto, si aparecen varias ideas.
    
    No incluyas explicaciones, encabezados, ni texto adicional: solo la respuesta en JSON. Ejemplo:

    {{
    "titulo": "Plancha abdominal",
    "categoria": "fuerza",
    "descripcion": "Apóyate en codos y pies; mantén el cuerpo recto; activa el abdomen"
    }}
    """
    return pregunta

 