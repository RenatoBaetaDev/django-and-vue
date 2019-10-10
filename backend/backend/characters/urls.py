from django.conf.urls import url

from .views import CharacterCreate, CharacterDestroy, CharacterGet, CharacterList, CharacterUpdate

urlpatterns = [
    url(r'characters/$', CharacterList.as_view()),
    url(r'characters/(?P<pk>\d+)/$', CharacterDestroy.as_view()),
    url(r'characters/add/$', CharacterCreate.as_view()),
    url(r'characters/get/(?P<pk>\d+)/$', CharacterGet.as_view()),
    url(r'characters/edit/(?P<pk>\d+)/$', CharacterUpdate.as_view()),
]
