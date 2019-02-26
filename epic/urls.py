from django.conf.urls import url
from . import views

urlpatterns=[
    url('^todat/$',views.image_today,name='image_today')
]
