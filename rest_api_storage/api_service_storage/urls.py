from django.urls import path
from . import views

urlpatterns = [path('service/photos/', views.ImageListFilterView.as_view(), name='photos'),]
