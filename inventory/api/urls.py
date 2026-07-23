from django.urls import path
from .import views


urlpatterns=[
    path('login/',views.login,name='login'),
    path("register_user/",views.register_user,name='user'),
    path("user_list/",views.user_list,name='user'),
    path("update_user/<int:pk>/",views.update_user,name='user'),
    path('add_supplier/',views.add_supplier,name='add_supplier'),
    path('update_supplier/<int:pk>/',views.update_Supplier,name='update_supplier'),
    path('delete_supplier/<int:pk>/',views.delete_supplier,name='delete_supplier'),
    path("register_manager/",views.register_manager,name='register_manager'),
    path("update_manager/<int:pk>/",views.update_manager,name='update_manager'),
    path("delete_manager/<int:pk>/",views.delete_manager,name='delete_mamager'),


   
]