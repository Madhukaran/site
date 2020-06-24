from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
from froala_editor import views


sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('', include('pwa.urls')),
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitempas.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
