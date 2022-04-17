from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, MovieForm
from users.models import Movie, UserProfile
from django.contrib import messages
from core.views import movie_detail

# Create your views here.


def user_login(request):
    method = request.method
    if method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse(' Authenticated successfully')
            else:
                return HttpResponse('username or password are invalid')
    else:
        form = LoginForm(request.POST)
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            UserProfile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


def addmovieform(request):
    method = request.method
    form = request.POST
    print(form)
    movieadded = "movie has been succesfully added to the watchlist"
    if method == "POST":

        # process the forms
        movieform = Movie()
        movieform.user = request.user
        movieform.movie_id = request.POST.get("movie")
        movieform.save()

        messages.success(
            request, "movie has been succesfully added to the watchlist")

        return redirect('/')
    else:
        form = MovieForm()
        return render(request, 'core/movie_detail.html', {"form": form})
