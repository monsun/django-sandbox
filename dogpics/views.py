import logging

#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import Context, loader

from dogpics.models import Album, Picture

logger = logging.getLogger(__name__)
# Views of dog pictures


def albums_view(request):
    albums_list = Album.objects.all()
    t = loader.get_template('dogpics/albums.html')
    c = Context({'albums_list': albums_list})
    return HttpResponse(t.render(c))


def album_view(request, album_id=None):
    if album_id is None:
        return HttpResponseNotFound('<h1>Album not found</h1>')

    album = Album.objects.get(pk=album_id)
    pictures = Picture.objects.filter(album=album)
    logger.info('Loaded pictures in album '+album.name+',', len(pictures))

    t = loader.get_template('dogpics/album.html')
    album_header = 'Album '+album.name+' by '+album.author.name
    c = Context({'album': album, 'album_header': album_header, 'pictures': pictures})
    return HttpResponse(t.render(c))