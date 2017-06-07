from django.conf.urls import url

from blog.views import home, post_detail, edit_post, add_post, del_post, add_comment, del_comment

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^(?P<pk>[0-9]+)/$', post_detail, name="post"),
    url(r'^add/$',add_post,name="add_post"),
    url(r'^(?P<pk>[0-9]+)/edit$', edit_post, name="edit"),
    url(r'^(?P<id>[0-9]+)/delete/$',del_post, name="del"),
    url(r'^(?P<pk>[0-9]+)/com$', add_comment, name="com"),
    url(r'^(?P<id>[0-9]+)/del/$', del_comment, name="delete"),

]
