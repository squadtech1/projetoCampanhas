from django.db import models

class DadosCadastrais(models.Model):

	nome = models.CharField(
		max_length=255,
		null=False,
		blank=False,
	)
	
	cpf = models.CharField(
 		max_length=14,
 		null=False,
 		blank=False
 	)
 
	
 	cnpj = models.CharField(
 		max_length=18,
 		null=False,
		blank=False
	)
		
	email = models.CharField(
		max_length=255,
		null=False,
		blank=False,
	)
	
	telefone = models.CharField(
		max_length= 100,
		null=False,
		blank=False
    )