from django.db import models

def upload_slider_image(instance,filename):
    return f'images/slider/{filename}'


class Slider(models.Model):
    title = models.CharField(max_length=100, blank=True)  
    image = models.ImageField(upload_to=upload_slider_image)         
    is_active = models.BooleanField(default=True,verbose_name='فعال/غیر فعال') 
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')   

    class Meta:
        verbose_name = "تصویر اسلایدر"      
        verbose_name_plural = "تصاویر اسلایدرها" 

    def __str__(self):
        return self.title or f"Slider Image {self.id}"
