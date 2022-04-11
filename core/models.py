from django.db import models
from stdimage.models import StdImageField

from uuid import uuid4

def get_file_path(_instance, filename):
	ext = filename.split('.')[-1]
	filename = f'{uuid4()}.{ext}'

	return filename


class Base(models.Model):
	criado = models.DateTimeField('Criado em', auto_now_add=True)
	atualizado = models.DateTimeField('Modificado em', auto_now=True)
	ativo = models.BooleanField('Ativo?', default=True)

	class Meta:
		abstract = True


class MarcaCarro(Base):
	nome = models.CharField('Nome', max_length=32)

	def __str__(self):
		return self.nome


class Carro(Base):
	marca = models.ForeignKey(MarcaCarro, verbose_name='Marca', on_delete=models.CASCADE)
	modelo = models.CharField('Modelo', max_length=64)
	ano = models.IntegerField('Ano')
	foto = StdImageField('Foto', upload_to=get_file_path, variations={'thumb': (1920, 1080, True)})
	destaque = models.BooleanField('Destaque?', default=False)

	class Meta:
		verbose_name = 'Carro'
		verbose_name_plural = 'Carros'

	def __str__(self):
		return self.modelo


class Vendedor(Base):
	nome = models.CharField('Nome', max_length=64)
	descricao = models.TextField('Descrição', max_length=128)
	email = models.EmailField('E-mail', max_length=128)
	telefone = models.CharField('Telefone', max_length=16)
	foto = StdImageField('Foto', upload_to=get_file_path, variations={'thumb': (400, 400, True)})

	class Meta:
		verbose_name = 'Vendedor'
		verbose_name_plural = 'Vendedores'

	def __str__(self):
		return self.nome
