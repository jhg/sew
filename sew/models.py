from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


# Sobreescribimos el campo de email para soptar al longitud total posible
User.email = models.EmailField(_('e-mail address'), blank=False, max_length=254)

