from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def usuarios(request):

    lista_usuarios = [
        {
            "nome": "Akira",
            "matricula": "2024017",
            "idade": 17,
            "cidade": "Belém"
        },
        {
            "nome": "Yasmin",
            "matricula": "2023154",
            "idade": 23,
            "cidade": "Curitiba"
        },
        {
            "nome": "Gael",
            "matricula": "2022781",
            "idade": 20,
            "cidade": "Manaus"
        },
        {
            "nome": "Luna",
            "matricula": "2024902",
            "idade": 18,
            "cidade": "Florianópolis"
        },
        {
            "nome": "Ícaro",
            "matricula": "2023560",
            "idade": 25,
            "cidade": "Salvador"
        }
    ]

    context = {
        "usuarios": lista_usuarios
    }

    return render(request, 'app/usuarios.html', context)