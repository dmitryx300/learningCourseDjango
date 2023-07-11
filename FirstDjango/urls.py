from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('item/<int:id>/', views.get_item),
    path('items/', views.items_list, name='Items')
]