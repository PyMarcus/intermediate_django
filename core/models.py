from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify  # create a valid url


class Base(models.Model):
    create = models.DateField("Create at", auto_now_add=True)
    modify = models.DateField("Update at", auto_now=True)
    active = models.BooleanField("Active?", default=True)

    class Meta:  # Its not create at database
        abstract = True


class Product(Base):
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price', max_digits=8, decimal_places=2)
    stoke = models.IntegerField('Stoke')
    image = StdImageField('Image', upload_to='products', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
