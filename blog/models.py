from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class PostCadastro(models.Model):

    sex_list = (
        ('0', 'Feminino'),
        ('1', 'Masculino'),
    )

    pais_list = (
        ('0', 'Brasil'),
        ('1', 'Outro'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    idade = models.CharField(max_length=200)
    endereço = models.CharField(max_length=200)
    sexo = models.CharField(max_length=1, choices=sex_list)
    país = models.CharField(max_length=1, choices=pais_list)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome