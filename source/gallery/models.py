from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from gallery.managers import PhotographyManager


# Create your models here.
class Photography(models.Model):
    description = models.CharField(verbose_name='Подпись', null=False, max_length=200)
    photo = models.ImageField(verbose_name='Фото', null=False, blank=True, upload_to='posts')
    author = models.ForeignKey(verbose_name='Автор', to=get_user_model(), related_name='photos', null=False, blank=False,
                               on_delete=models.CASCADE)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    objects = PhotographyManager()
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
