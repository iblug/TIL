from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album

# Create your views here.
def index(request):
    if request.method == "POST":
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums:index')
    else:
        form = AlbumForm()
        albums = Album.objects.all()
    context = {
        'form': form,
        'albums': albums,
    }
    return render(request, 'albums/index.html', context)