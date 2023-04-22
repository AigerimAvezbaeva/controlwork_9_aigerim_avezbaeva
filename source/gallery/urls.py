from django.urls import path

from gallery.views import PhotosListView, PhotoView, PhotoCreateView, PhotoUpdateView, PhotoDeleteView

urlpatterns = [
    path('', PhotosListView.as_view(), name='index'),
    path('photos/<int:pk>/', PhotoView.as_view(), name='photo'),
    path('photos/create/', PhotoCreateView.as_view(), name='photo_create'),
    path('photos/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photos/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]
