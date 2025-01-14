from rest_framework import mixins, generics, filters, status
from rest_framework.response import Response

from django.http import HttpResponse
from django.views import View
# Create your views here.
from swift_lyrics.models import Lyric, Album, Song
from swift_lyrics.serializers.serializer import LyricSerializer, BaseSongSerializer, BaseAlbumSerializer, \
    AlbumDetailSerializer, \
    SongDetailSerializer, LyricSerializer, SongSerializer, LyricDetailSerializer


class HealthCheckView(View):
    """
    Checks to see if the site is healthy.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse("ok")


class AlbumIndex(mixins.ListModelMixin,
                 generics.GenericAPIView):
    serializer_class = BaseAlbumSerializer

    def get_queryset(self):
        return Album.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AlbumDetail(mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                generics.GenericAPIView):
    serializer_class = AlbumDetailSerializer

    def get_queryset(self):
        return Album.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class SongIndex(mixins.ListModelMixin,
                 generics.GenericAPIView):
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class SongDetail(mixins.RetrieveModelMixin,
                 mixins.DestroyModelMixin,
                generics.GenericAPIView):
    serializer_class = SongDetailSerializer

    def get_queryset(self):
        return Song.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class APIIndex(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    """
    For finding lyrics
    Ordering values can be: 'text', 'song__name', 'song__album__name'
    """
    serializer_class = LyricDetailSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'song__name', 'song__album__name']
    ordering_fields = ['text', 'song__name', 'song__album__name']


    def get_queryset(self):
        return Lyric.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class APIDetail(mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    serializer_class = LyricDetailSerializer

    def get_queryset(self):
        return Lyric.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
