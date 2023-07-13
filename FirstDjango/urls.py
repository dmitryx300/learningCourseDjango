from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('about/', views.about, name='About'),
    path('item/<int:id>/', views.get_item, name='item-detail'),
    path('items/', views.items_list, name='Items')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)