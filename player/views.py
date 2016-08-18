from player.forms import UserForm,PlayerForm
from django.template import RequestContext
from django.shortcuts import render_to_response, Http404, render,get_object_or_404
from models import User

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        player_form = PlayerForm(data=request.POST)
        if user_form.is_valid() and player_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            player = player_form.save(commit = False)
            player.user = user

            if 'avatar' in request.FILES:
                player.avatar = request.FILES['avatar']

            player.save()
            registered = True
        else:
            print user_form.errors, player_form.errors
    else:
        user_form = UserForm()
        player_form = PlayerForm()
    return render_to_response(
        'player/register.html',
        {'user_form':user_form, 'player_form':player_form,'registered':registered},
        context)

def userview (request, user_username):
    user = get_object_or_404(User, username=user_username)
    return render_to_response('player/userview.html',{'user':user})