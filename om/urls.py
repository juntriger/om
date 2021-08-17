from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('opman/', include('opman.urls')),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'), # / 페이지에 해당하는 urlpatterns
]

handler404 = 'common.views.page_not_found'