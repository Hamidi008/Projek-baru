# URL PROJEK #

from django.urls import path

from . import views

urlpatterns = [
	path('delete/<update_id>/', views.update, name='update'),
	path('delete/<delete_id>', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]