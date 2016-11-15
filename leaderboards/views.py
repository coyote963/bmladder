from django.shortcuts import render
from django.db import connection
# Create your views here.
def index(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename, rating, player_id FROM player ORDER BY rating DESC;")
			playerlist = cursor.fetchall()
		finally:
			cursor.close()
	return render(request,
		'leaderboards/index.html',
		{'playerlist':playerlist})
def playerview(request, pk):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT killer_name, victim_name, dateoccurred, weapon, matchup_id FROM matchup WHERE killer_id = (%s) OR victim_id = (%s) ORDER BY dateoccurred DESC;",
				(pk, pk))
			matchuplist = cursor.fetchall()
		finally:
			cursor.close()
	return render(request, 
		'leaderboards/player.html',
		{'matchuplist':matchuplist})
