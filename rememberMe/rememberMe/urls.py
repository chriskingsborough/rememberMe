"""rememberMe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from person import views as person
from event import views as event
from index import views as index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', index.logout),
    url(r'^sign_up/', index.create_user),
    url(r'^sign_in/', index.sign_in),
    url(r'^create_event/', event.create_event),
    url(r'^view_event_list/', event.view_event_list),
    url(r'^update_event/', event.edit_event),
    url(r'^view_event/', event.view_event),
    url(r'^delete_event/', event.delete_event),
    url(r'^create_person/', person.create_person),
    url(r'^view_person_list/', person.view_person_list),
    url(r'^update_person/', person.edit_person),
    url(r'^view_person/', person.view_person),
    url(r'^delete_person/', person.delete_person)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
