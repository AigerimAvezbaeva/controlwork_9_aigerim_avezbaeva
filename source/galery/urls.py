from django.urls import path

from galery.views import PhotosView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('', PhotosView.as_view(), name='index'),
    path('photos/<int:pk>/', PhotoView.as_view(), name='photo'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]
