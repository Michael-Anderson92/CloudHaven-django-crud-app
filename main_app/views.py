from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.views import LoginView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

from .models import Album, Picture, User

# Authorization
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Imports for the signup
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('album_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or a bad POST request
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})



# About view


# === User Views ===
# class UserList(ListView):
#     model = User
#     template_name = 'users/index.html'  # Customize path if needed

# class UserDetail(DetailView):
#     model = User
#     template_name = 'users/detail.html'

# === Album Views ===
class AlbumList(ListView):
    model = Album
    template_name = 'albums/album_index.html'

class AlbumDetail(DetailView):
    model = Album
    template_name = 'albums/album_detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['title', 'cover_image']  # Fields to include in the form
    template_name = 'albums/album_form.html'
    success_url = '/albums/'  # Redirect to the album index after creating a new album

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['title', 'description']  # Editable fields
    template_name = 'albums/album_form.html'
    success_url = '/albums/'

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'albums/album_confirm_delete.html'  # Specify the correct path
    success_url = '/albums/'  # Redirect after deletion


class Home(LoginView):
    # specify a template
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')




# # === Picture Views ===
# class PictureList(ListView):
#     model = Picture
#     template_name = 'pictures/picture_index.html'
#     context_object_name = 'picture_list'

# class PictureDetail(DetailView):
#     model = Picture
#     template_name = 'pictures/picture_detail.html'

# class PictureCreate(CreateView):
#     model = Picture
#     fields = ['image']  # Include the `image` field
#     template_name = 'pictures/picture_form.html'

# class PictureUpdate(UpdateView):
#     model = Picture
#     fields = ['image']  # Editable field
#     template_name = 'pictures/picture_form.html'

# class PictureDelete(DeleteView):
#     model = Picture
#     success_url = '/pictures/'

# # === Association Views ===
# # Add a user to an album
# def add_user_to_album(request, album_id, user_id):
#     album = get_object_or_404(Album, id=album_id)
#     user = get_object_or_404(User, id=user_id)
#     album.users.add(user)  # Create the association
#     return redirect('album_detail', pk=album_id)

# # Remove a user from an album
# def remove_user_from_album(request, album_id, user_id):
#     album = get_object_or_404(Album, id=album_id)
#     user = get_object_or_404(User, id=user_id)
#     album.users.remove(user)  # Remove the association
#     return redirect('album_detail', pk=album_id)

# # Add a picture to an album
# def add_picture_to_album(request, album_id, picture_id):
#     album = get_object_or_404(Album, id=album_id)
#     picture = get_object_or_404(Picture, id=picture_id)
#     album.pictures.add(picture)  # Create the association
#     return redirect('album_detail', pk=album_id)

# # Remove a picture from an album
# def remove_picture_from_album(request, album_id, picture_id):
#     album = get_object_or_404(Album, id=album_id)
#     picture = get_object_or_404(Picture, id=picture_id)
#     album.pictures.remove(picture)  # Remove the association
#     return redirect('album_detail', pk=album_id)
