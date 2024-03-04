from django.db import models

# Create your models here.


class Shaharlar(models.Model):
    name = models.CharField(max_length=200)
    text=models.TextField(max_length=900)
    image=models.ImageField(upload_to='student/')
    category=models.ForeignKey('Category', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Mamlakat'
        verbose_name_plural = 'Mamlakatlar'

    def __str__(self):
        return self.name




class Category(models.Model):
    name = models.CharField(max_length=200)


    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def __str__(self):
        return self.name

