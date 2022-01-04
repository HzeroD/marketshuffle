from django.contrib import admin
from django.urls import path, include
from . import views
from .views import StockCreate, StockUpdate, StockDelete, ClientList, ClientCreate, ClientUpdate, ClientDelete

urlpatterns = [
path('', views.Home.as_view(), name='home'),
path('about/', views.about, name='about'),
path('stocks/', views.stocks_index,name='stocks_index'),
path('stocks/create',views.StockCreate.as_view(), name='stocks_create'),
path('stocks/<int:stock_id>/', views.stocks_detail, name='stocks_detail'),
path('stocks/<int:pk>/update', views.StockUpdate.as_view(),name='stocks_update'),
path('stocks/<int:pk>/delete', views.StockDelete.as_view(),name='stocks_delete'),
path('stocks/<int:stock_id>/add_order', views.add_order, name='add_order'),
path('clients/create',views.ClientCreate.as_view(),name='clients_create'),
path('clients/<int:pk>/update/',views.ClientUpdate.as_view(),name='clients_update'),
path('clients/',views.ClientList.as_view(), name='clients_index'),
path('clients/<int:pk>/delete',views.ClientDelete.as_view(),name='clients_delete'),
path('clients/<int:pk>',views.ClientDetail.as_view(), name='clients_detail'),
path('stocks/<int:stock_id>/assoc_client/<int:client_id>/', views.assoc_client, name='assoc_client'),
path('accounts/signup/', views.signup, name='signup'),

]