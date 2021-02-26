from django.db import models
from django.utils.translation import gettext_lazy as _

class Brand(models.Model):
    """ Model representing a brand """
    class Meta:
        verbose_name = _('brand')

    name = models.CharField(_('brand'), max_length=60, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    Model representing a device catery, like Monitor, Motherboard and so on
    """
    class Meta:
        verbose_name = _('category')

    name = models.CharField(_('category'), max_length=60, unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        return self.name
