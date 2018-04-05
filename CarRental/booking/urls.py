
from django.conf.urls import url


from . import views
urlpatterns = [
url(r'delete/', views.delete),
url(r'bookingHistory/', views.bookingHistory),
url(r'book/', views.book),
url(r'bill/', views.bill),
url(r'carlist/', views.carlist),
url(r'', views.booking),
]