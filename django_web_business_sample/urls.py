from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    # Path Admin
    path('admin/', admin.site.urls),

    # Paths Core
    path('', include('core.urls')),

    # Paths Contact
    path('contact/', include('contact.urls')),

    # Paths Services
    path('services/', include('services.urls')),

    # Paths Blogs
    path('blog/', include('blog.urls')),

    # Pages Blogs
    path('page/', include('pages.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# CK Editor 5
urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)