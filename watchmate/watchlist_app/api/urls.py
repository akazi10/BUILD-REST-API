
from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import (ReviewList, WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewDetail)
urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream'),
    path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='stream-details'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    path('stream/<int:pk>/review/',ReviewList.as_view(),name='review-list'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(), name='review-detail'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
