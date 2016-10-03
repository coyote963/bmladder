from player.models import Profile
from django.contrib.auth.models import User
def save_profile(backend, user, response, *args, **kwargs):
    
    if backend.name == 'steam':
        try:
            user.profile.ingamename = kwargs['uid']
        except AttributeError:

    
            player = Profile(
                user = user,
                steamid = kwargs['details']['player']['steamid'],
                ingamename = kwargs['details']['player']['personaname'],
                steamimage = kwargs['details']['player']['avatarmedium'],
                )
            player.save()