from django.contrib import admin
from django.urls import path, include
from .views import  home, add_annonce

urlpatterns = [
    path('', home, name='home'),
    path('annonce/add', add_annonce, name='add_annonce'),
    # path('annonce/detail/<uuid:pk>', views.annonceDetaiView, name='annonce_detail'),
    # path('annonce/favorite/<uuid:pk>', views.favorite, name='favorite_annonce'),
    # path('annonce/favorite/', views.annonce_favorite_list, name='favorite_list'),
    # path('annonce/message/<int:user_pk>', views.message_mp, name='message'),  
    # path('annonce/messages/', views.message_list, name='message_list'),
    # path('annonce/list', annonceListView.as_view(), name='annonce_list'),
    # path('annonce/delete/<uuid:pk>', AnnonceDeletelView.as_view(), name='annonce_delete'),
    # path('annonce/update/<uuid:pk>', views.updateAnnonce, name='annonce_update'),
]