from django.db import models
import jdatetime
from ckeditor.fields import RichTextField

# Create your models here.




class Blog(models.Model):
    class PublishManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=True)
        
    PUBLISH_CHOICE = {
        True:'Publish',
        False: "Draft"
    }

    title = models.CharField(max_length=200)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_created=True)
    slug = models.SlugField(unique=True,allow_unicode=True)
    image = models.ImageField(upload_to="blog_img/")
    status = models.BooleanField(
        choices=PUBLISH_CHOICE, default=False
    )

    objects = models.Manager()
    published = PublishManager()

    def persian_date(self):

        jalali_date = jdatetime.datetime.fromgregorian(date=self.published_at)

        days = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنجشنبه", "جمعه"]
        day_of_week = days[jalali_date.weekday()]
        day = jalali_date.day

        months = [
            "فروردین",
            "اردیبهشت",
            "خرداد",
            "تیر",
            "مرداد",
            "شهریور",
            "مهر",
            "آبان",
            "آذر",
            "دی",
            "بهمن",
            "اسفند",
        ]
        month = months[jalali_date.month - 1]

        year = jalali_date.year

        return f"{day_of_week} {day} {month} {year}"

    def __str__(self):
        return self.title
