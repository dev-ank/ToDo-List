from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('post_home',views.post_home,name='post_home'),
	path('delete_post/<int:todoid>',views.delete_post,name='delete_post'),
]