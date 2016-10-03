from player.models import Profile
from django.contrib.auth.models import User
def save_profile(backend, user, response, *args, **kwargs):
    
    if backend.name == 'steam':
        try:
            user.profile.ingamename = kwargs['uid']
        except AttributeError:

            import pdb; pdb.set_trace()
            player = Profile(
                user = user,
                ingamename = kwargs['details']['player']['steamid']
                )
            player.save()