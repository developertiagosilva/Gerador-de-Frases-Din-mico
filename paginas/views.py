import random
from datetime import datetime
from django.shortcuts import render

def frase_motivacional(request):
    frases = [
        "Console-se, o código funcionou na primeira tentativa pelo menos uma vez na história.",
        "A indentação correta cura dores de cabeça que nenhum café consegue curar.",
        "Um bom programador não é aquele que não erra, mas aquele que sabe ler o Traceback.",
        "Grandes softwares começam com pequenos 'Hello World' bem compreendidos.",
        "Se o código está difícil de explicar, foi uma má ideia. Se for fácil, talvez seja boa."
    ]
    
    frase_do_dia = random.choice(frases)
    agora = datetime.now().strftime('%H:%M:%S')
    
    contexto = {
        'frase': frase_do_dia,
        'autor': 'Mestres do Django',
        'hora_atual': agora
    }
    
    return render(request, 'paginas/frase.html', contexto)