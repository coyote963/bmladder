from django.contrib import admin

# Register your models here.
from ladder.models import Tournament,Match,Participant, Comment
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Participant)
admin.site.register(Comment)