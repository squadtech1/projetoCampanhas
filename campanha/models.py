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

	idDadosCadastrais = models.ForeignKey(DadosCadastrais, on_delete=models.CASCADE, verbose_name= 'Id dados')
	dadosCadastrais = models.OneToOneField(DadosCadastrais, on_delete=models.CASCADE,verbose_name= 'Relacionamento dados/doador')
	doacao = models.CharField(max_length= 100)
	quantidade = models.CharField(max_length= 10)

class EntidadeOrganizadora(models.Model):

	campanha = models.ForeignKey("Campanha")
	idDadosCadastrais = models.ForeignKey(DadosCadastrais, on_delete=models.CASCADE, verbose_name= 'Id dados')
	dadosCadastrais = models.OneToOneField(DadosCadastrais, on_delete=models.CASCADE, verbose_name= 'Relacionamento dados/entidade')
	responsavel = models.CharField(max_length= 100)

class Campanha(models.Model):

	doadores = models.ManyToManyField(Doador)
	nome = models.CharField(max_length=255)
	beneficiados = models.CharField(max_length=255)

class DuracaoCampanha(models.Model):
	idCampanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, verbose_name= 'Id campanha')
	campanha = models.OneToOneField(Campanha, on_delete=models.CASCADE, verbose_name= 'Relacionamento Duração/Campanha')
	inicio = models.DateField('inicio da campanha')
	fim = models.DateField('fim da campanha')

class Meta(models.Model):
	idCampanha = models.ForeignKey(Campanha, on_delete=models.CASCADE, verbose_name= 'Id campanha')
	descricao = models.CharField(max_length=100)
	status = models.CharField(max_length=30)

class Composicao(models.Model):
	idMeta = models.ForeignKey(Meta, on_delete=models.CASCADE, verbose_name= 'Id Meta')
	objeto = models.CharField('Item a ser doado', max_length=100)
	quantidade = models.CharField(max_length=100)
	status = models.CharField(max_length=30)
	Observacao = models.CharField(max_length=300, null= True, blank= True)
	