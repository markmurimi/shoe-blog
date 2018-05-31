from . import views
from django.conf.urls import url,include

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^home/',views.home,name = 'home')
]
