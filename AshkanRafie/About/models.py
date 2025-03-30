from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Bio(models.Model):
    بیوگرافی = RichTextField()
    تحصیلات_دانش = RichTextField()
    فعالیت = RichTextField()
    علاقمندی = RichTextField()
    هنر = RichTextField()
    مهارت = RichTextField()
    image1 = models.ImageField(null=True)
    image2 = models.ImageField(null=True)
    image3 = models.ImageField(null=True)



    def __str__(self):
        return "bio"