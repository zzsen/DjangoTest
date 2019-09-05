"""testPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from . import view, testdb, search, search2
from django.contrib import admin


urlpatterns = [
    url(r'^$', view.hello),
    url('hi', view.hi),
    url(r'^insert$', testdb.insert),
    url(r'^get$', testdb.get),
    url(r'^update$', testdb.update),
    url(r'^delete$', testdb.delete),
    url(r'^search$', search.search),
    url(r'^search-form$', search.search_form),
    url(r'^search-post$', search2.search_post),
    url(r'^admin/', admin.site.urls),
]
