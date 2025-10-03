from django.db import models
import uuid


class Comment(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    text = models.TextField(verbose_name='متن')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    email = models.EmailField(verbose_name='ایمیل')
    parent=models.ForeignKey('Comment',null=True,blank=True,on_delete=models.CASCADE,related_name='replies',verbose_name='پاسخ به')
    verify_code=models.UUIDField(default=uuid.uuid4,editable=False,verbose_name='کد تایید')
    is_active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    
    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'
        
    def __str__(self):
        return f'{self.name},{self.email}'
