from django.db import models
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='categories')
    is_enable = models.BooleanField(_('Is enable'), default=True)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now=True)

    class Meta:
        db_table = _('categories')
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description', blank=True))
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('Is_enable'), default=False)
    Categories = models.ManyToManyField('Category', verbose_name=_('Categories'), blank=True)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now=True)

    class Meta:
        db_table = _('products')
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('Product'), on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=50)
    file = models.FileField(_('File'), upload_to='files/')
    is_enable = models.BooleanField(_('Is enable'), default=False)
    created_time = models.DateTimeField(_('Created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('Updated time'), auto_now=True)

    class Meta:
        db_table = _('files')
        verbose_name = _('File')
        verbose_name_plural = _('Files')