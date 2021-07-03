from django.urls import path

from . import views

urlpatterns = [
    path('add', views.edit_thimble, name='create_thimble'),
    path('', views.main, name='main'),
    path('<int:thimble_id>/edit', views.edit_thimble, name='edit_thimble'),
    path('<int:thimble_id>/info', views.thimbles_info, name='thimbles_info'),
    path('<int:thimble_id>/delete', views.del_thimbles, name='del_thimbles'),
    path('souvenir', views.souvenir, name='souvenir'),
    path('classic', views.classic, name='classic'),
    path('russia', views.russia, name='russia')
]