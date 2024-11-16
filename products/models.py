from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name='parent', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Title', max_length=50)
    description = models.TextField(verbose_name='Description', blank=True)
    avatar = models.ImageField('Avatar', blank=True, upload_to='categories/')
    is_enable = models.BooleanField('Is enable', default=True)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('Description', blank=True)
    avatar = models.ImageField('Avatar', blank=True, upload_to='products/')
    is_enable = models.BooleanField('Is_enable', default=False)
    Categories = models.ManyToManyField('Category', verbose_name='Categories', blank=True)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name='Product', on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    file = models.FileField('File', upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField('Is enable', default=False)
    created_time = models.DateTimeField('Created time', auto_now_add=True)
    updated_time = models.DateTimeField('Updated time', auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'