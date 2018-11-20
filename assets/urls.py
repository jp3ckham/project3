from django.conf.urls import url
from django.contrib import admin
from . import views
appname='assets'
urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', 'assets.views.index', name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<asset_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/(?P<asset_id>[0-9]+)/$', views.edit, name='edit'),
    url(r'^delete(?P<asset_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^search/', views.search, name='search'),
]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.index, name='index'),
#     path('<int:asset_id>/', views.detail, name='detail'),
# ]