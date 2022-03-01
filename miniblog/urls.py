from ast import pattern
from django.contrib import admin
from django.urls import path
from blog import views
from django.urls import path,include
from django.views.static import serve as mediaserve
from django.conf import settings
from miniblog import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.user_logout,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.user_login,name="signin"),
    path('addpost/',views.add_post,name="addpost"),
    path('update_Post/<int:pk>',views.update_post,name="updatepost"),
    path('delete_post/<int:pk>',views.delete_post,name="deletepost"),

]
