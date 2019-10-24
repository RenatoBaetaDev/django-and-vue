from django.conf.urls import url

from .views import (
    Upload,
)

urlpatterns = [
    # url(r'characters/$', CharacterList.as_view()),
    # url(r'characters/(?P<pk>\d+)/$', CharacterDestroy.as_view()),
    url(r'files/upload/$', Upload.as_view()),
    # url(r'characters/get/(?P<pk>\d+)/$', CharacterGet.as_view()),
    # url(r'characters/edit/(?P<pk>\d+)/$', CharacterUpdate.as_view()),
]