from django.shortcuts import render , redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User, auth
from .models import Blog
from django.contrib import messages
from .forms import *
# Create your views here

def home(request):
	blogs=  Blog.objects.all()
	return render(request, "posts/home.html",{'blogs': blogs})

def login(request):
	if request.method == 'POST':
		username= request.POST ['username']
		password= request. POST ['password']
		
		user= auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect("/")
		else:
			messages.info(request,'invalid password or username')
			return redirect("login") 
	return render(request, "posts/login.html",{})

def addblog(request):
	if request.method == 'POST':
		blogtopic= request.POST['blogtopic']
		blogsummary= request.POST['blogsummary']
		blogcontent= request.POST['blogcontent']
		draft= request.POST.get('draft',False)
		image= request.FILES.get('image')
		date_published= request.POST.get('datetime.now')


		blogs=Blog()
		blogs= Blog.objects.create(blogtopic=blogtopic, blogcontent=blogcontent, draft=False,date_published=date_published, image=image)
		return redirect ('/')
		

	return render(request, "posts/addblog.html",{})

def register(request):
	if request.method == 'POST':
		first_name= request.POST['first_name']
		last_name= request.POST['last_name']
		username= request.POST['username']
		email= request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		
		

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'username taken')
				return redirect ('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'email taken')
				return redirect ('register')
			else:
				user=User()
				user= User.objects.create_user(username=username, password= password1, email=email, first_name= first_name, last_name=last_name)
				user.save();
				return redirect('login')
	
		messages.info(request,'password not matching')
		return redirect ('register')
	else:
		return render(request, 'posts/register.html',{})

def logout(request):
	auth.logout(request)
	return redirect('/')

def minimum_size(width=None, height=None):

    def validator(image):
        if not image.is_image():
            raise ValidationError('File should be image.')

        (errors, image_info) = ([], image.info()['image_info'])
        if width is not None and image_info['width'] < width:
            errors.append('Width should be > {} px.'.format(width))
        if height is not None and image_info['height'] < height:
            errors.append('Height should be > {} px.'.format(height))
        raise ValidationError(errors)

    return validator
