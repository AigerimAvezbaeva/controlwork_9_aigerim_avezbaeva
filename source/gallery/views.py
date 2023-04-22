from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from gallery.forms import PhotoForm
from gallery.models import Photography


# Create your views here.

class PhotosListView(ListView):
    model = Photography
    template_name = 'index.html'
    context_object_name = 'photos'

    def get_queryset(self):
        return super(PhotosListView, self).get_queryset().order_by('-created_at')


class PhotoView(DetailView):
    template_name = 'photo.html'
    model = Photography
    context_object_name = 'photo'

    def get(self, request, *args, **kwargs):
        favorite = request.GET.get('favorite')
        if favorite:
            request.user.favorites.add(favorite)
        not_favorite = request.GET.get('not_favorite')
        if not_favorite:
            request.user.favorites.remove(not_favorite)
        return super().get(request, *args, **kwargs)

class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    form_class = PhotoForm
    model = Photography
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('photo', kwargs={'pk':self.object.pk})


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name ='photo_update.html'
    form_class = PhotoForm
    model = Photography
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_photo.html'
    model = Photography
    context_object_name = 'photo'
    success_url = reverse_lazy('index')
