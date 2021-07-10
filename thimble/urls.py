from django.urls import path

from . import views

urlpatterns = [
    path('add', views.edit_thimble, name='create_thimble'),
    path('', views.main, name='main'),
    path('thimbles', views.thimbles, name='thimbles'),
    path('<int:thimble_id>/edit', views.edit_thimble, name='edit_thimble'),
    path('<int:thimble_id>/info', views.thimbles_info, name='thimbles_info'),
    path('<int:thimble_id>/delete', views.del_thimbles, name='del_thimbles'),
    path('russia', views.russia, name='russia'),
    path('countries', views.countries, name='countries'),
    path('souvenir', views.souvenir, name='souvenir'),
    path('add_country', views.create_countries, name='create_country'),
    path('add_city', views.create_city, name='create_city'),
    path('<int:country_id>/country_info', views.country_info, name='country_info'),
    path('<int:city_id>/city_info', views.city_info, name='city_info'),
    path('church', views.church, name='church'),
    path('working', views.working, name='working'),
    path('promisel', views.promisel, name='promisel'),
    path('sova', views.sova, name='sova'),
    path('people', views.people, name='people'),
    path('all_cities', views.all_cities, name='all_cities'),
    path('<int:city_id>/del_cities', views.del_cities, name='del_cities'),
    path('<int:city_id>/edit_city', views.create_city, name='edit_city'),
]