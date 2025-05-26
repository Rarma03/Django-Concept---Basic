from django.urls import path

from . import views


urlpatterns = [
    # route : localhost:8000/firstservice
    path('', views.all_chai, name='all_chai'),
    # route : localhost:8000/firstservice/order
    path('order/', views.order, name='order'),

    # route : localhost:8000/firstservice/chai_id
    path('<int:chai_id>/', views.chai_detail, name='chai_detail')
]