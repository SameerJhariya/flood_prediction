from django.conf.urls import url, include
import views

urlpatterns = [
	url(r'^$', views.floods),
	url(r'^data/', views.data),
	url(r'^data1/', views.data1),
]