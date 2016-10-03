from django import template
from datetime import datetime
from player.models import Profile
register = template.Library()

@register.inclusion_tag('content_box.html')
def show_content_box(user, content):
	date = datetime.now()
	context = {'date': date}
	try:
		profile = user.profile
	except Profile.DoesNotExist:
		context['content'] = content
		context['username'] = user.username
		return context
	else:
		context['avatar'] = profile.avatar
		context['content'] = content
		context['username'] = user.username
		return context
@register.inclusion_tag('content_box_simple.html')
def show_content_box_simple(author, content):
	date = datetime.now()
	context = {'date': date}
	context['author'] = author
	context['content'] = content
	return context