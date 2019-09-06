from django.urls import path
from . import views

urlpatterns = [path('service/photos/', views.ImagesListView.as_view(), name='photos'),
               path('service/photos/<int:id>/', views.ImageDetailView.as_view(), name='detail-image'),
               path('service/photo/', views.ImageSaveStorage.as_view(), name='photo'),
               path('service/', views.InfoService.as_view(), name='info'),
               path('', views.redirect_service, name='redirect_service'),
               ]
