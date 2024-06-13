from django.contrib import admin
from django.urls import path, include
from .views import HomePageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', HomePageView.as_view(), name='landing'),
]
