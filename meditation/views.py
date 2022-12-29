from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import Soundscape, Mood, Category, UserSession

from django.http import JsonResponse, HttpResponseBadRequest

# Create your views here.


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account Successfully Created for {user}')
            return render(request, 'login.html')

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.info(request, "Username or Password is Incorrect")
            return render(request, 'login.html')

    context = {}
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return render(request, 'logout.html')


@login_required(login_url='login/')
def index_page(request, category_slug=None):
    sounds = Soundscape.objects.all()
    moods = Mood.objects.all()

    return render(request, 'index.html', {'sounds': sounds, 'moods': moods})


@login_required(login_url='login/')
def meditate_page(request):

    user = request.user.id

    moods = Mood.objects.filter(mood="Content")
    new_moods = moods[0]
    return render(request, 'meditate.html', {'new_moods': new_moods})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def ajax_test(request):
    user = request.user

    if is_ajax(request):
        if request.method == 'POST':
            testing = request.POST
            print('testing', testing)

            print('moods_before_meditation', testing['moods_before_meditation'])
            print('meditation_music', testing['meditation_music'])
            print('meditation_time', testing['meditation_time'])

            UserSession.objects.create(user=user,
                                       moods_before_meditation=testing['moods_before_meditation'],
                                       meditation_duration=testing['meditation_time'],
                                       song_name=testing['meditation_music']
                                       )
            return JsonResponse({'status': 'Meditation Session Added'})
        return JsonResponse({'status': 'Invalid Request'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid Request')


@login_required(login_url='login/')
def history_page(request):
    user_id = request.user.id
    user_history = UserSession.objects.filter(user_id=user_id).values()

    return render(request, 'history.html', {'user_history': user_history})


@login_required(login_url='login/')
def attributes_page(request):
    return render(request, 'attributes.html')
