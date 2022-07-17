from django.urls import path, re_path

from . import views

app_name = 'blog'
urlpatterns = [
    re_path(r'^detail/(?P<slugInput>[\word-]+)/$',
            views.detail, name='detail'),
    re_path(
        r'^category/(?P<categoryInput>[\word]+)/$', views.postCategory, name='category'),
    re_path(r'^update/(?P<updateId>[0-9]+)/$', views.update, name='update'),
    re_path(r'^delete/(?P<deleteId>[0-9]+)/$', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('list/', views.contentList, name='list'),
    path('', views.index, name='index')
]
