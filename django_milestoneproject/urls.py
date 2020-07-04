"""django_milestoneproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from mp.views import get_mp_list, create_an_item, edit_an_item, toggle_status

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_mp_list),
    url(r'^add$', create_an_item),
    url(r'^edit/(?P<id>\d+)$', edit_an_item),
    url(r'^toggle/(?P<id>\d+)$', toggle_status),
    url(r'^index$', index, name="index"),
    url(r'^accounts/', include(accounts_urls))

]
