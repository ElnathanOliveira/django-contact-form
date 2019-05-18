from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=128,verbose_name='Nome')
    email = models.CharField(max_length=128,verbose_name='E-mail')
    subject = models.CharField(max_length=128,verbose_name='Assunto')
    message = models.TextField(verbose_name='Mensagem')