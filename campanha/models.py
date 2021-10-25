from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db.models.manager import ManagerDescriptor

class DadosCadastrais(models.Model):

	nome = models.CharField(max_length=255)

	cpf = models.CharField(max_length=14)	
 	
	cnpj = models.CharField(max_length=18)		
	
	email = models.EmailField(max_length=100)	
	
	telefone = models.CharField(max_length= 100)

class Doador(models.Model):

	IdDadosCadastrais = ForeignKey(DadosCadastrais, on_delete=models.CASCADE, verbose_name= 'Os Dados Cadastrais')
	
	DadosCadastrais = models.OneToOneField(DadosCadastrais, on_delete=models.CASCADE,verbose_name= 'Os Dados Cadastrais')

	doacao = models.CharField(max_length= 100)

	quantidade = models.CharField(max_length= 10)

class EntidadeOrganizadora(models.Model):

	idDadosCadastrais = ForeignKey(DadosCadastrais, on_delete=models.CASCADE, verbose_name= 'Os Dados Cadastrais')

	DadosCadastrais = models.OneToOneField(DadosCadastrais, on_delete=models.CASCADE, verbose_name= 'Os Dados Cadastrais')

	Responsavel = models.CharField(max_length= 100)

class Campanha(models.Model):

	doadores = models.ManyToManyField(Doador)

	nome = models.CharField(max_length=255)

	beneficiados = models.CharField(max_length=255)
	