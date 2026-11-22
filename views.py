from django.shortcuts import render, redirect, get_object_or_404
from .models import Song
from .forms import SongForm

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'player/song_list.html', {'songs': songs})


def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('song_list')
    else:
        form = SongForm()
    return render(request, 'player/upload_song.html', {'form': form})

def delete_song(request, pk):
    song = get_object_or_404(Song, pk=pk)
    song.delete()
    return redirect('song_list')
