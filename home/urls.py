from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('under_construction', views.index_404, name='under_construction'),
]
