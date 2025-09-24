from django.db import models

#-----------

def upload_to_main(instance, filename):
    return f'images/main/{filename}'

class Main(models.Model):
    title = models.CharField(max_length=100,verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    instagram = models.URLField(blank=True,null=True,verbose_name='لینک اینستاگرام')
    linkdin = models.URLField(blank=True,null=True,verbose_name='لینک لینکدین')
    github = models.URLField(blank=True,null=True,verbose_name='لینک گیت هاب')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    image = models.ImageField(upload_to=upload_to_main,null=True,blank=True,verbose_name='عکس')
    
    def __str__(self):
        return self.title  
    
    class Meta:
        verbose_name= 'صفحه اصلی '
        verbose_name_plural= 'صفحه های اصلی'  
        
#-----------

def upload_to_projects(instance, filename):
    return f'images/projects/{filename}'

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان پروژه')
    description = models.TextField(verbose_name='توضیحات پروژه')
    image = models.ImageField(upload_to=upload_to_projects, blank=True, null=True, verbose_name='عکس پروژه')
    link = models.URLField(blank=True, null=True, verbose_name='لینک پروژه')
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='دسته‌بندی پروژه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'نمونه‌کار'
        verbose_name_plural = 'نمونه‌کارها'
    
#-----------

def upload_to_blog(instance, filename):
    return f'images/blog/{filename}' 

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    content = models.TextField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to=upload_to_blog, blank=True, null=True, verbose_name='عکس مقاله')
    author = models.CharField(max_length=100, verbose_name='نویسنده')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')
    published = models.BooleanField(default=True, verbose_name='منتشر شده؟')
    category = models.CharField(max_length=100, blank=True, null=True, verbose_name='دسته‌بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

#-----------

def upload_to_about(instance, filename):
    return f'images/about/{filename}'

class About(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')
    title = models.CharField(max_length=200, verbose_name='عنوان شغلی')
    description = models.TextField(verbose_name='توضیحات درباره من')
    profile_image = models.ImageField(upload_to=upload_to_about, blank=True, null=True, verbose_name='عکس پروفایل')
    birthday = models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')
    email = models.EmailField(blank=True, null=True, verbose_name='ایمیل')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره تماس')
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name='آدرس')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درباره من'
        verbose_name_plural = 'درباره من'

#-----------

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام فرستنده')
    email = models.EmailField(verbose_name='ایمیل فرستنده')
    subject = models.CharField(max_length=200, verbose_name='موضوع پیام')
    message = models.TextField(verbose_name='متن پیام')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال')
    read = models.BooleanField(default=False, verbose_name='خوانده شده؟')

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name = 'پیام تماس'
        verbose_name_plural = 'پیام‌های تماس'

#-----------



