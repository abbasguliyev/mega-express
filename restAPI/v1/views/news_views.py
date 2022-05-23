from rest_framework import status, generics
from rest_framework.response import Response
from news.models import News
from restAPI.v1.serializers.news_serializers import NewsSerializer

class NewsListCreateAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class NewsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'slug'