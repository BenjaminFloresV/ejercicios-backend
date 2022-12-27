from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/agregar', views.add_cat, name='add_cat'),
     path('/listar', views.get_cats, name='get_cats'),
]