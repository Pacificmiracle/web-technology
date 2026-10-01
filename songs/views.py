from django.shortcuts import redirect,render, get_object_or_404
from .models import Song
from songs.forms import SongForm
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView

#def song_list(request):
##    songs = Song.objects.filter(
        #is_published=False
   # ).order_by('-release_date')

 #   return render(
  #      request,
   #     'song_list.html',
   #     {'songs': songs}
   # )

class SongListView(ListView):
    model = Song
    template_name = 'song_list.html'
    context_object_name = 'songs'

    def get_queryset(self):
        return Song.objects.filter(is_published=True).order_by('-release_date')

class SongDetailView(DetailView):
    model = Song
    pk_url_kwarg = 'song_id'
    template_name = 'song_detail.html'
    context_object_name = 'song'
  

def song_create(request):
    if request.method == 'POST':
        form = SongForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'song_form.html', {'form': form})


class UploadSong(View):
    def get(self, request):
        return render(request, 'song_form.html', {'form': SongForm()})

    def post(self, request):
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song-list')
        return render(request, 'song_form.html', {'form': form})