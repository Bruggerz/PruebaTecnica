from django.conf.urls import url
from restaurant import views

urlpatterns=[
    url(r'^api/restaurant$', views.restaurant_list),
    url(r'^api/insertaRestaurant$', views.insertarRestaurant),
    url(r'^api/actualizarRestaurant$',views.actualizarRestaurant),
    url(r'^api/eliminarRestaurant$',views.eliminarRestaurant),
    url(r'^api/filtrarRestaurante$',views.restaurantFiltrado)
]