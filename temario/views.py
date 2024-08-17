from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .forms import TemarioForm
import requests
from xhtml2pdf import pisa

def index(request):
    if request.method == 'POST':
        form = TemarioForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data

            # Define la solicitud a la API de ChatGPT
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {os.getenv("OPENAI_API_KEY")}',
                    'Content-Type': 'application/json'
                },
                json={
                    'model': 'gpt-4',
                    'messages': [
                        {'role': 'system', 'content': 'Eres un generador de temarios de cursos.'},
                        {'role': 'user', 'content': f'Genera un temario para un curso llamado {datos["titulo_curso"]} que se cursará durante {datos["dias_curso"]} días, en horario {datos["horario"]}, con {datos["participantes"]} participantes, impartido por {datos["instructor"]}. El curso tiene como objetivo {datos["objetivo"]} y el temario incluye: {datos["descripcion_temario"]}. El nivel del curso es {datos["nivel"]} y la modalidad es {datos["modalidad"]}. Materiales necesarios: {datos["materiales"]}.'}
                    ]
                }
            )
            
            temario = response.json()['choices'][0]['message']['content']
            return render(request, 'resultado.html', {'temario': temario})

    else:
        form = TemarioForm()

    return render(request, 'index.html', {'form': form})


def generar_pdf(request):
    template_path = 'resultado.html'
    context = {'temario': request.POST.get('temario')}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="temario.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )

    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=400)

    return response
