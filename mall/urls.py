from django.conf.urls import url
from mall.views import IndexView


urlpatterns = [
    url(r'index/', IndexView.as_view(), name='index')
]
