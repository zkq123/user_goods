from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('vote', views.vote, name='vote'),
    path('detail', views.detail, name='xxxx'),
    path('<int:user_id>/message', views.message, name='message'),
    path('register',views.register, name='register'),
    path('denglu', views.denglu, name='denglu'),
    path('<int:user_id>/message_2', views.message_2, name='message_2'),
    path('<int:user_id>/message_2_1', views.message_2_1, name='message_2_1'),
    path('<int:user_id>/message_3', views.message_3, name='message_3'),
    path('<int:user_id>/message_4', views.message_4, name='message_4'),
    path('<int:user_id>/message_4_1', views.message_4_1, name='message_4_1'),
    path('found', views.found, name='found'),
    path('found_1', views.found_1, name='found_1'),
    path('<int:user_id>/found_2', views.found_2, name='found_2'),
    path('<int:user_id>/found_3', views.found_3, name='found_3'),
    path('look', views.look, name='look'),
    path('<int:user_id>/add_goods', views.add_goods, name='add_goods'),
    path('<int:user_id>/save_goods', views.save_goods, name='save_goods'),
    path('<int:user_id>/check', views.check, name='check'),
    path('<int:user_id>/change', views.change, name='change'),
    path('<int:user_id>/change_1', views.change_1, name='change_1'),
    path('<int:user_id>/<goods_bh>/change_2', views.change_2, name='change_2'),
    path('<int:user_id>/check_change', views.check_change, name='check_change')

]
