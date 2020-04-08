from django.urls import path
from . import views

urlpatterns = [
    path('', views.year_list, name='year_list'),
    path('modeltypes/', views.modeltype_list, name='modeltype_list'),
    path('years/<int:pk>', views.year_detail, name='year_detail'),
    path('modeltypes/<int:pk>', views.modeltype_detail, name='modeltype_detail'),
    path('years/new', views.year_create, name='year_create'),
    path('modeltypes/new', views.modeltype_create, name='modeltype_create'),
    path('years/<int:pk>/edit', views.year_edit, name='year_edit'),
    path('modeltypes/<int:pk>/edit', views.modeltype_edit, name='modeltype_edit'),
    path('years/<int:pk>/delete', views.year_delete, name='year_delete'),
    path('modeltypes/<int:pk>/delete', views.modeltype_delete, name='modeltype_delete')
]