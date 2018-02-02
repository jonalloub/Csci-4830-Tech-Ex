from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('new/', views.article_new, name='article_new'),
	path('<int:article_id>/', views.article, name='article'),
]
