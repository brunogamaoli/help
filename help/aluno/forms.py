from django import forms
from .models import Aluno

class PostForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ('nome', 'nascimento', 'telefone' ,'cpf', 'email', 'rua', 'bairro', 'cidade', 'nivel_conhecimento')

