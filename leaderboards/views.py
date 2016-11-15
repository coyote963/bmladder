from django.shortcuts import render
from django.db import connection
# Create your views here.
def index(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT ingamename FROM player")
		playerlist = cursor.fetchall()
	return render(request,
		'leaderboards/index.html',
		{'playerlist':playerlist})
