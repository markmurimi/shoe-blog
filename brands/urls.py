from . import views
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^home/',views.home,name = 'home'),
    url(r'^search_results/', views.search_results, name='search_results'),
    url(r'^post/', views.new_post, name='postImage'),
    url(r'^brandDetails/(?P<brand_id>[0-9]+)/$', views.brandDetails, name= 'brandDetails'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)