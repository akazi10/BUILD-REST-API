# from rest_framework import serializers

from watchlist_app.models import WatchList,StreamPlatform,Review 
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer,ReviewSerializer
# from rest_framework .decorators import api_view
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework import generics
# from rest_framework import mixins



class ReviewList(generics.ListCreateAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Review.objects.all()
    serializer_class = ReviewSerializer    

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)





class StreamPlatformAV(APIView):

    def get(self,request):
        platform= StreamPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)

    def post (self,request):
        serializer= StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)




class WatchListAV(APIView):


    def get(self,request):
        movies =WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)    

class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerializer(
            platform, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):


    def get(self,request,pk):
        try:
            movie= WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'movie not found'},status=status.HTTP_404_NOT_FOUND)    
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        movie =WatchList.objects.get(pk=pk)
        serializer =WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_REQUEST)    

    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.discription = validated_data.get('discription',instance.discription)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance


# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#       movies = Movie.objects.all()
#       serializer = MovieSerailzer(movies,many=True)
#       return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerailzer(data=request.data)
#         if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data)
#         else:
#            return Response(serializer.errors)







# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer= MovieSerailzer(movie)
#         return Response(serializer.data)

 
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerailzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#              return Response(serializer.errors)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response()





