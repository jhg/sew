from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Sobreescribiendo el campo username para nombres de usuario de 254 caracteres
User.username = models.CharField(_('username'), max_length=254, unique=True,
        help_text=_('Required. 254 characters or fewer. Letters, numbers and '
                    '@/./+/-/_ characters'))

# Sobreescribimos el campo de email para usar la longitud total posible
User.email = models.EmailField(_('e-mail address'), blank=False, max_length=254)

