"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from books.views import index, list_of_users

schma_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="Book API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="tufliyev@tuit.uz"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

from django.contrib.staticfiles.views import serve as serve_static

def _static_butler(request, path, **kwargs):
    """
    Serve static files using the django static files configuration
    WITHOUT collectstatic. This is slower, but very useful for API 
    only servers where the static files are really just for /admin

    Passing insecure=True allows serve_static to process, and ignores
    the DEBUG=False setting
    """
    return serve_static(request, path, insecure=True, **kwargs)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('books.urls')),
    path('swagger/', schma_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schma_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
    path('users/', list_of_users, name='users'),
    path('', index, name='index'),

]

urlpatterns += [
    re_path(r'static/(.+)', _static_butler)
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
