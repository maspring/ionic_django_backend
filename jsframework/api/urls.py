from django.conf.urls import url
from jsframework.api.views.picture_views import PictureView

urlpatterns = [

    url(r'^pictures/$', PictureView.as_view())
    #    url(r'^pictures/\d', 'IMG_1470.jpg')
]