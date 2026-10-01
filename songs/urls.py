from django.urls import path
from songs import views

urlpatterns = [
   
    path('', views.SongListView.as_view(), name='song_list'),                 # /songs/
    path('create/', views.song_create, name='song_create'),  # /songs/create/
    path('new/', views.UploadSong.as_view(), name='song_new'),  # /songs/new/
    #path('update/<int:song_id>/', views.song_update, name='song_update'),  # /songs/update/1/
    path('<int:song_id>/', views.SongDetailView.as_view(), name='song_detail'),  # /songs/1/

]
