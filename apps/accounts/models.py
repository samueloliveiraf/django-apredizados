from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    photo = models.ImageField(
        'Image',
        upload_to='photos',
    )
    cell_phone = models.CharField(
        'Celular',
        max_length=16
    ) 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Perfil do usuario'
        verbose_name_plural = 'Perfis dos usuarios'

    def __str__(self):
        return self.user.username