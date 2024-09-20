from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('contact/',views.contact_view,name='contact'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]
