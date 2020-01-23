from django.contrib import admin
from django.urls import include, path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
    path('test_page/', views.test_page, name='test_page'),
    path('about/', views.about, name='about'),
    path('polls/', include('polls.urls')),
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
