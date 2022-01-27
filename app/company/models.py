from django.db import models
from app.accounts.managers import UserManager


class Company(models.Model):
    #managers = models.ManyToManyField(AbstractBaseUser, related_name='Gerente', blank = True)
    name = models.CharField (max_length=255, verbose_name= 'Nome', unique=True, error_messages= {"unique": "Nome já cadastrado."})
    cnpj = models.CharField (max_length=18, verbose_name= 'CNPJ', unique= True, error_messages={"unique": 'CNPJ já cadastrado!'})
    email = models.EmailField(max_length=255, verbose_name= 'Email', unique=True, error_messages= {"unique": "Email já cadastrado."})
    status = models.CharField(max_length=15, verbose_name='ativo')
    city =  models.CharField(max_length=255, verbose_name='Cidade')
    bairro = models.CharField(max_length=255, verbose_name='Bairro')
    is_active =models.BooleanField (default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts", verbose_name="Ativar Cadastro")
    USERNAME_FIELD = "email"
    objects = UserManager()



    class Meta:
        verbose_name_plural = 'Companhias'

    def __str__(self):
        return self.name     
