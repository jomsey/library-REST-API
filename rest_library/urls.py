from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework_jwt import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('library.urls')),
    path('__auth__/', include('rest_framework.urls', namespace='rest_framework')),
    path('token-auth/',views.obtain_jwt_token),

]

if settings.DEBUG:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))

