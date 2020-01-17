from django.db import models


# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True, default=None)
    image = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
