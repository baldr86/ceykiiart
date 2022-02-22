from distutils.command.upload import upload
from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class FanArt (models.Model):
    titulo = models.TextField(max_length=100)
    imagen = models.ImageField(upload_to="fanart")
    fechaPublicacion = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(FanArt, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo, self.fechaPublicacion
        
    def get_absolute_url(self):
        
        return reverse("post_detail", kwargs={ # hay que cambiar el post_detail
            
            'slug': self.slug
            })


class OriginalWork (models.Model):
    titulo = models.TextField(max_length=100)
    imagen = models.ImageField(upload_to="originalwork")
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(OriginalWork, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo, self.fechaPublicacion
        
    def get_absolute_url(self):
        
        return reverse("post_detail", kwargs={ # hay que cambiar el post_detail
            
            'slug': self.slug
            })