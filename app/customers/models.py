from enum import unique
from django.db import models
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    class Meta:
        verbose_name = _('cutomer')

    name = models.CharField(_('name'), max_length=40)
    ruc = models.CharField(_('ruc'), max_length=40, unique=True)
    email = models.EmailField(_('email', unique=True))
    telephone = models.CharField(_('telephone'), max_length=40, blank=True, null=True)
    address = models.CharField(_('address'), max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.name
