from django.urls import path
from .views import IndexView, DetailView, AlbumCreateView, AlbumDeleteview, AlbumUpdateView, UserFormview

app_name = 'music'

urlpatterns = [
    # /music/
    path('', IndexView.as_view(), name='index'),

    # /music/712/
    path('<int:pk>/', DetailView.as_view(), name='detail'),

    #/music/album/add
    path('album/add/', AlbumCreateView.as_view(), name='album-add'),

    # /music/album/2
    path('album/<int:pk>/', AlbumUpdateView.as_view(), name='album-update'),

    # /music/album/2
    path('album/<int:pk>/delete', AlbumDeleteview.as_view(), name='album-delete'),

    # register_form
    path('register/', UserFormview.as_view(), name='register'),
    # /music/712/
    # path('<int:album_id>/favourite', favourite, name='favourite')
]
