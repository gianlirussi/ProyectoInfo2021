from django import forms
from .models import Pregunta
from .models import Respuesta
from .models import Categoria

class PreguntaForm(forms.ModelForm):

    class Meta:
        model = Pregunta
        fields = ('pregunta','id_categoria')

class RespuestaForm(forms.ModelForm):

    class Meta:
        model = Respuesta
        fields = ('opcion','puntaje','id_pregunta')

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('categoria','descripcion')



