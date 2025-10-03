from django.urls import path
from . import views
from .views import send_email_box,CommentListAndCreateComment,verify_email, send_verify_email

app_name = 'comments'

urlpatterns = [
    path('comment/verify/<uuid:code>/', views.verify_email, name='verify_comment'),#ارسال ایمیل به کاربر
    path('comment/send-verify/', views.send_verify_email, name='send_verify_email'),#تایید لینک در ایمیل 
    path('send_email_box/',send_email_box,name='send_email_box'),#باکس ارسال ایمیل
    path('comments/', CommentListAndCreateComment.as_view(), name='comments')#لیست کامنت ها و اضافه کردن کامنت جدید
]



