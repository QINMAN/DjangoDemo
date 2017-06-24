from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
                       (r"^$",views.index),
                       (r"^article/detail/(\d+)",views.detail)

)
