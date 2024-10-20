

from django.contrib import admin
from django.urls import path,include
from django_app import views

handler404 = 'django_app.views.handler404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('api/', include('polls.api_urls')),
    path('accounts/', include('accounts.urls')),  # Include accounts URLs
]

