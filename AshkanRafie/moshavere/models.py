from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class personalMoshavere (models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(default=None)
    def __str__(self):
        return self.title
    

class businessMoshavere (models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(default=None)
    def __str__(self):
        return self.title
    
class cardMoshavere(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to="moshavere_img/")