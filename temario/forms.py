from django import forms

class TemarioForm(forms.Form):
    titulo_curso = forms.CharField(label='Título del curso', max_length=100)
    dias_curso = forms.IntegerField(label='Días que se cursará')
    horario = forms.CharField(label='Horario del curso', max_length=50)
    participantes = forms.IntegerField(label='Cantidad de participantes')
    instructor = forms.CharField(label='Nombre del instructor', max_length=100)
    objetivo = forms.CharField(label='Objetivo del curso', widget=forms.Textarea)
    descripcion_temario = forms.CharField(label='Descripción del temario', widget=forms.Textarea)
    nivel = forms.ChoiceField(choices=[('basico', 'Básico'), ('intermedio', 'Intermedio'), ('avanzado', 'Avanzado')], label='Nivel del curso')
    modalidad = forms.ChoiceField(choices=[('presencial', 'Presencial'), ('online', 'Online')], label='Modalidad')
    materiales = forms.CharField(label='Materiales necesarios', widget=forms.Textarea)
