from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('<int:post_id>/edit', views.edit, name='edit'),
]