"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1.views import hello,test_sf,test_log
from app2.views import test_db,test_ll

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/$',hello,name='hello'),
    url(r'^test_sf/$',test_sf,name='test_sf'),
    url(r'^test_db/$',test_db,name='test_db'),
    url(r'^test_log/',test_log,name="test_log"),
    url(r'^test_ll/',test_ll,name="test_ll"),
]
