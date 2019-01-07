from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('frigg/', include('frigg.urls')),
    path('admin/', admin.site.urls),
]