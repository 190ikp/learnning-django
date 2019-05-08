from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('add', views.add, name='add'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]