from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان بلاگ")
    slug = models.SlugField(unique=True, max_length=200, verbose_name="Slug")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="نویسنده")
    content = models.TextField(verbose_name="متن بلاگ")
    excerpt = models.TextField(blank=True, verbose_name="خلاصه")  # برای نمایش کوتاه در لیست
    cover_image = models.ImageField(upload_to='blog_covers/', blank=True, null=True, verbose_name="عکس")
    published_date = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")
    is_published = models.BooleanField(default=True, verbose_name="منتشر شود؟")
    tags = models.CharField(max_length=200, blank=True, verbose_name="برچسب ها")

    class Meta:
        ordering = ['-published_date']  # جدیدترین‌ها اول
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ‌ها"

    def __str__(self):
        return self.title
