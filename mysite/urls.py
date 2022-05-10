from cgitb import handler
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import Image, ImageDisplay


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('image/', Image.as_view(), name = 'image'),
    path('image/<int:pk>/', ImageDisplay.as_view(), name = 'image_display'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)