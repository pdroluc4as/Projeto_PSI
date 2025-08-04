from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.db.models.signals import post_save # type: ignore
from django.dispatch import receiver # type: ignore

#acima são bibliotecas padrões necessárias do Django, e abaixo nossos models

from .fabricante import Fabricante
from .Categoria import Categoria
from .Produto import Produto

PERFIL = (
    (1, "Admin"),
    (2, "Usuario"),
)
from .usuario import Usuario