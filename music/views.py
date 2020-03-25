from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponse
from .models import Album, Song
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from .forms import UserForm


# def index(request):
#     all_albums = Album.objects.all()
#     snippet for without template
#     html = ""
#     for album in all_albums:
#         url = "/music/" + str(album.id) + "/"
#         html += "<a href ='" + url + "'>" + album.album_name + "</a><br>"
#     return HttpResponse(html)
#     template = 'music/index.html'
# content = {
#     'all_albums': all_albums
# }
# return render(request, template, context=content)


# def detail(request, album_id):
#     try:
#         album = Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album Doesn't Exist")
#     album = get_object_or_404(Album, pk=album_id)
#     template = 'music/details.html'
#     content = {
#         'album': album,
#     }
#     return render(request, template, context=content)
#

# def favourite(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         selected_song = album.song_set.get(pk=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/details.html', {
#             'album': album,
#             'error_message': 'You didnt select a valid song',
#         }
#                       )
#     else:
#         selected_song.is_favourite = True
#         selected_song.save()
#         return render(request, 'music/details.html', {'album': album})

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'


class AlbumCreateView(generic.CreateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']


class AlbumUpdateView(generic.UpdateView):
    model = Album
    fields = ['artist', 'album_name', 'genre', 'album_logo']


class AlbumDeleteview(generic.DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormview(generic.FormView):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # clean data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # return user object if credsientials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user=user)
                    redirect('music:index')

        return render(request, self.template_name, {'form': form})
