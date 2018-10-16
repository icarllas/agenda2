from django import forms

from .models import Post, PostCadastro

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'text',]

class PostCadastroForm(forms.ModelForm):

    class Meta:
        model = PostCadastro
        fields = ['nome', 'cidade','estado','idade','endereço','sexo','país']