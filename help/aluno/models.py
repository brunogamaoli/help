from django.db import models
from django.utils import timezone

class Aluno(models.Model):

	A = 'Excelente'
	B = 'Bom'
	C = 'Regular'
	D = 'Ruim'

	CHOICES_NIVEL = (
		(A , 'Excelente'),
		(B , 'Bom'),
		(C , 'Regular'),
		(D , 'Ruim'),
	)

	nome = models.CharField(max_length=100)
	#nascimento = models.CharField("Data de Nascimento", max_length=8, default ='')
	nascimento = models.DateField(help_text="Digitar no modelo Dia/Mes/Ano")
	telefone = models.CharField(max_length=12)
	cpf = models.CharField(help_text="Apenas os 11 numeros do CPF", max_length=11, unique = True)
	email = models.EmailField(max_length=100, default = '')
	data_entrada = models.DateTimeField(default=timezone.now)
	rua = models.CharField(max_length=100, default = '')	
	bairro = models.CharField(max_length=100, default = '')
	cidade = models.CharField(max_length=100, default = '')
	numero_matricula = models.CharField(max_length=20, unique = True, default="")
	#status = models.CharField(max_length=11, default = '')
	#atalho = models.SlugField('Atalho', default = '')

	nivel_conhecimento = models.CharField(
		max_length=100,
		choices = CHOICES_NIVEL,
	)

	def publish(self):
		self.data_entrada = timezone.now()
		self.save()

	def __str__(self):
		return self.nome
