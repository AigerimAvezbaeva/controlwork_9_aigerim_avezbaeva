from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from galery.forms import PhotoForm
from galery.models import Photography


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


class PhotosView(ListView):
    template_name = 'index.html'
    model = Photography
    context_object_name = 'photos'

    def get_queryset(self):
        return super(PhotosView, self).get_queryset().order_by('-created_at')


class PhotoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'photo_create.html'
    form_class = PhotoForm
    model = Photography

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect('photo', pk=photo.pk)
        context = {}
        context['form'] = form
        return self.render_to_response(context)


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'photo_update.html'
    form_class = PhotoForm
    model = Photography
    context_object_name = 'photo'

    # def get_success_url(self):
    #     return reverse('profile', kwargs={'upk': self.request.user.pk, 'pk': self.object.pk})

    def get_success_url(self):
        return reverse('index')


class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'delete_photo.html'
    model = Photography
    context_object_name = 'photo'
    success_url = reverse_lazy('index')
