from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('add', views.add, name='add'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript'))
]