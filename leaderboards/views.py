from django.shortcuts import render
from django.db import connection
import numpy
from collections import Counter
# Create your views here.
def index(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename, rating, player_id FROM player ORDER BY rating DESC LIMIT 100;")
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
def graph(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT rating FROM player ORDER BY rating ASC;")
		ratinglist = cursor.fetchall()
		ratinglist = map((lambda x: x[0]), ratinglist)
		indices = map((lambda x: str(x)), createrange(ratinglist,20))
		bins = createfrequency(ratinglist, 120)

		cursor.execute("SELECT weapon FROM matchup ORDER BY dateoccurred DESC LIMIT 1000;")
		weaponlist = cursor.fetchall()
		weaponcounts = Counter(weaponlist)
		weapons, frequency = weaponcounts.keys(), weaponcounts.values()

	return render(request,
		'leaderboards/graph.html',
		{'ratinglist':ratinglist,
		'indices':indices,
		'bins':bins,
		'weapons':weapons,
		'frequency':frequency})

def createrange(ratinglist, step):
	minimum =  (ratinglist[0] / step) * step
	maximum =  (ratinglist[-1] /step ) *step + step
	return range(minimum, maximum+ step, step)
def createfrequency(ratinglist, step):
	minimum =  (ratinglist[0] / step) * step
	maximum =  (ratinglist[-1] /step ) *step + step
	numbins = len(range(minimum, maximum+ step, step))
	return list(numpy.histogram(ratinglist, numbins)[0])