from django.urls import path
from . import views

urlpatterns = [
    # Home view
    path('', views.Home.as_view(), name='home'),

    # About view
    path('about/', views.about, name='about'),

    # User-related URLs
    # path('users/', views.UserList.as_view(), name='user_index'),
    # path('users/<int:pk>/', views.UserDetail.as_view(), name='user_detail'),

    # Album-related URLs
    path('albums/', views.AlbumList.as_view(), name='album_index'),
    # path('albums/<int:pk>/', views.AlbumDetail.as_view(), name='album_detail'),
    path('albums/create/', views.AlbumCreate.as_view(), name='album_create'),
    path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='album_update'),
    path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='album_delete'),

    # Picture-related URLs
    # path('pictures/', views.PictureList.as_view(), name='picture_index'),
    # path('pictures/<int:pk>/', views.PictureDetail.as_view(), name='picture_detail'),
    # path('pictures/create/', views.PictureCreate.as_view(), name='picture_create'),
    # path('pictures/<int:pk>/update/', views.PictureUpdate.as_view(), name='picture_update'),
    # path('pictures/<int:pk>/delete/', views.PictureDelete.as_view(), name='picture_delete'),

    # Association-related URLs
    # path('albums/<int:album_id>/add-user/<int:user_id>/', views.add_user_to_album, name='add-user-to-album'),
    # path('albums/<int:album_id>/remove-user/<int:user_id>/', views.remove_user_from_album, name='remove-user-from-album'),
    # path('albums/<int:album_id>/add-picture/<int:picture_id>/', views.add_picture_to_album, name='add-picture-to-album'),
    # path('albums/<int:album_id>/remove-picture/<int:picture_id>/', views.remove_picture_from_album, name='remove-picture-from-album'),
    path('accounts/signup/', views.signup, name='signup'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
