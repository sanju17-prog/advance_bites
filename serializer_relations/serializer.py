from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration', 'singer']

class SingerSerializer(serializers.ModelSerializer):
    # NOSONAR
    # songs = serializers.StringRelatedField(many=True, read_only=True) 
    # songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # songs = SongSerializer(many=True, read_only=True) # '''this is nested serialization'''
    # songs = serializers.HyperlinkedRelatedField(many = True, read_only = True, view_name = 'song-detail')
    songs = serializers.HyperlinkedIdentityField(view_name='song-detail', many=True)
    # NOSONAR
    # songs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')
    # songs = serializers.SlugField(read_only=True)
    class Meta:
        model = Singer
        fields = ['id', 'name','gender','songs']