from re import search
from django.shortcuts import render
from django.http import Http404
from .models import Song 
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json




class SongList(APIView):

    def get(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)

        return Response(serializer.data)

        
    def post(self, request):
        serializer = SongSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        

class SongDetails(APIView):

    def get_song(self, pk):
        try: 
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        song = self.get_song(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        song = self.get_song(pk)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        song = self.get_song(pk)
        song.delete()
        return Response(status=status.HTTP_200_OK)

class SongLike(APIView):
    
    def get_song(self, pk):
        try: 
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
            raise Http404


    def get(self, request, pk):
        song = self.get_song(pk)
        serializer = SongSerializer(song)
        return Response(serializer.data['artist'])
       


    def put(self, request, pk):
        song = self.get_song(pk)
        # song.data['likes'] += 1
        song.likes += 1
        song.save()
        serializer = SongSerializer(song)
        
        
        return Response(serializer.data,status=status.HTTP_200_OK)
       


      