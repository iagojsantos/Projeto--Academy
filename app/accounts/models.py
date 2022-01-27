import email
from enum import unique
from msilib import add_tables
from tabnanny import verbose
from unicodedata import name
from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from app.common import choices
from app.accounts.managers import UserManager
from cpf_field.models import CPFField


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255, verbose_name= "Nome")
    email = models.EmailField(max_length=255, verbose_name= "Email", unique=True, error_messages= {"unique": "Email já cadastrado."})
    cpf = CPFField (max_length=21, verbose_name='CPF',  unique=True, error_messages= {"unique": "CPF já cadastrado"})
    phone = models.CharField(max_length=21, verbose_name= "Telefone", blank=True, null=True)
    is_staff = models.BooleanField(default=False, help_text= "Designates whether the user can log into this admin site.", verbose_name="Acesso ao DashBoard")
    is_active =models.BooleanField (default=True, help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts", verbose_name="Ativar Cadastro")
    type = models.PositiveIntegerField(choices= choices.TYPE_USER, blank=True, default=0, verbose_name="Tipo de usuário", editable=False)
    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.name

class ManagerUser(models.Manager):
    def __init__(self, *args, **kwargs):
        self.type = kwargs.pop("type", True)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(type=self.type)

    def create(self, **kwargs):
        kwargs.update({"type": self.type})
        return super().create(**kwargs)

class Admin(User):
    objects = ManagerUser(type = choices.TYPE_USER.admin)

    class Meta:
        proxy= True
        verbose_name = "Administrador"
        verbose_name_plural = "Admnistradores"

class Customer(User):
    objects = ManagerUser(type = choices.TYPE_USER.customer)

    class Meta:
        proxy= True
        verbose_name ="Cliente"
        verbose_name_plural = "Clientes"

    def save(self, *args, **kwargs):
        self.is_superuser = False
        self.type = 1
        return super().save(*args, **kwargs)

