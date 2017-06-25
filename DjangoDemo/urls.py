from django.conf.urls import patterns, include, url
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoDemo.views.home', name='home'),
    # url(r'^DjangoDemo/', include('DjangoDemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
                       url(r"^",include("DjangoDemo.blog.urls")),

                       (r"^hello$",views.hello),
                       (r"^temp$",views.temp),
                       (r"^student$",views.studentList)
)
