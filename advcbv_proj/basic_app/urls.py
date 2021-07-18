from django.conf.urls import url
from basic_app import views

app_name='basic_app'

urlpatterns = [
    url('^$', views.SchoolListView.as_view(), name='list'),
    url('^st/$', views.SchoolListViewSt.as_view(), name='list_st'),
    url('^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url('^st/(?P<pk>\d+)/$', views.SchoolDetailViewSt.as_view(), name='detailst'),
    url('^create/$', views.SchoolCreateView.as_view(), name='create'),
    url('^st/createst/$', views.SchoolCreateViewSt.as_view(), name='createst'),
    url('^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url('^st/updatest/(?P<pk>\d+)/$', views.SchoolUpdateViewSt.as_view(), name='updatest'),
    url('^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
    url('^st/deletest/(?P<pk>\d+)/$', views.SchoolDeleteViewSt.as_view(), name='deletest'),

]
