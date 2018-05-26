
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^gst/', views.add_product, name='add_product'),
    url(r'^chart/',views.chart,name='chart'),

]


