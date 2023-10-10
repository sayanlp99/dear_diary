from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>/', views.delete_entry, name='delete_entry'),
    path('show/<int:id>/', views.show_entry, name='show'),
    path('edit/<int:id>/', views.edit_entry, name='edit')
]
