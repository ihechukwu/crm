from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('my-login',views.my_login, name='my-login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create-record',views.create_record, name='create-record'),
    path('logout', views.my_logout, name='logout'),
    path('view-record/<int:pk>', views.view_record, name='view-record'),
    path('delete-record/<int:pk>', views.delete_record, name='delete-record'),
]
 