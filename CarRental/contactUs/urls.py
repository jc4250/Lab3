from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'feedback/', views.feedback),
    url(r'contactUs/', views.contactUs),
    url(r'', views.contactUs),
]