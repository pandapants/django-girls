from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),

]

# That means if you enter http://127.0.0.1:8000/post/5/ into
# your browser, Django will understand that
# you are looking for a view called
# post_detail and transfer the information
# that pk equals 5 to that view.
