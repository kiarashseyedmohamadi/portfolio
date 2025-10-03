from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from .forms import CommentForm
from .models import Comment
import uuid
from django.views.generic import ListView
from django.urls import reverse
from django.contrib import messages

#-------------

# ثبت ایمیل کاربر و ارسال لینک به ایمیل
def send_verify_email(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        if email:
            code=str(uuid.uuid4())
            link=request.build_absolute_uri(reverse('comments:verify_comment',args=[code]))
            subject = 'تایید ایمیل برای ثبت کامنت'
            message = f'برای فعال شدن فرم کامنت روی لینک زیر کلیک کنید:\n{link}'
            send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,[email], fail_silently=False )
            request.session['email_to_verify']=email
            request.session['code_verify']=code
            return render(request, 'comments/email_sent.html', {'email': email})
        else:
            messages.error(request,'لطفا ایمیل معتبر وارد کنید')
            return redirect('comments:comments')
            
    else:
        return render(request,'comments/send_email_box.html')


#-------------

# تایید ایمیل
def verify_email(request, code):
    if request.session.get('code_verify') == str(code):
        email = request.session.get('email_to_verify')
        # ایمیل تایید شد
        request.session['email_verified'] = email
        messages.success(request, f"ایمیل {email} با موفقیت تایید شد ✅")
    else:
        messages.error(request, "لینک تایید معتبر نیست ❌")

    return redirect('comments:comments')



#-------------


# فرم ارسال و لیست کامنت
class CommentListAndCreateComment(View):
    template_name = 'comments/comment_list_and_add.html'

    def get(self, request):
        comments = Comment.objects.filter(is_active=True).order_by('-create_at')
        email_verified = request.session.get('email_verified', False)
        if email_verified:
            form = CommentForm()    
        else:
            form = None
        return render(request, self.template_name, {'comments': comments,'form': form,'verified_email': email_verified})

    def post(self, request):
        email_verified = request.session.get('email_verified', False)
        if not email_verified:
            messages.error(request, "لطفاً ابتدا ایمیل خود را تایید کنید.")
            return redirect('comments:comments')

        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "کامنت شما ثبت شد ✅ بعد از تایید مدیر نمایش داده می‌شود.")
            return redirect('comments:comments')
        else:
            comments = Comment.objects.filter(is_active=True).order_by('-create_at')
            return render(request, self.template_name, {'comments': comments,'form': form,'verified_email': email_verified })


 #------------- 


#نمایش باکس ایمیل
def send_email_box(request):
    return render (request,'comments/send_email_box.html')


#-------------



