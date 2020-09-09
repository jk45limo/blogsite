from django.urls import path
from . import views
 
urlpatterns= [
path("", views.home, name="home"),
path("blogs/", views.blogpage, name="blogs"),
path("addblog/", views.addblog, name="addblog"),
path("drafts/", views.drafts, name="drafts"),
path("register/", views.register, name="register"),
path("login/", views.login, name="login"),
path("logout/", views.logout, name="logout"),

]


