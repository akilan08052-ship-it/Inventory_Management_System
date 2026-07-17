from django.urls import path
from .import views


urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.user_in,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_supplier/',views.register_supplier,name='register_supplier'),
    path('add_catogery/',views.add_catogery,name='add_catogery'),
    path('add_product/',views.add_product,name='add_product'),
    path('register_purchase/',views.register_purchase,name='register_purchase'),
    path('add_unit/',views.add_unit,name='add_unit'),
    path('view_supplier/',views.view_supplier,name='view_supplier')
   
]