from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('kawasaki/', include('kawasaki.urls')),
    path('kago/', include('kago.urls')),
    path('krico/', include('krico.urls')),
    path('estriper/', include('estriper.urls')),
]