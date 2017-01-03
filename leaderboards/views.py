from django.shortcuts import render
from django.db import connection
import urllib2
import json
import numpy
from collections import Counter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename, rating, player_id, steamid, active FROM player ORDER BY rating DESC;")
			allplayers = cursor.fetchall()
			players = Paginator(allplayers,100)
			page = request.GET.get('page')
			try:
				playerlist = players.page(page)
			except PageNotAnInteger:
				playerlist = players.page(1)
			except EmptyPage:
				playerlist = players.page(paginator.num_pages)
		finally:
			cursor.close()
	return render(request,
		'leaderboards/index.html',
		{'players':playerlist})

def indexrecent(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename, rating, player_id, steamid, active, lastplayed FROM player ORDER BY lastplayed DESC;")
			allplayers = cursor.fetchall()
			players = Paginator(allplayers,100)
			page = request.GET.get('page')
			try:
				playerlist = players.page(page)
			except PageNotAnInteger:
				playerlist = players.page(1)
			except EmptyPage:
				playerlist = players.page(paginator.num_pages)
		finally:
			cursor.close()
	return render(request,
		'leaderboards/index.html',
		{'players':playerlist})

def indexdm(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename, rating, player_id, steamid, active FROM dmplayer ORDER BY rating DESC;")
			allplayers = cursor.fetchall()
			players = Paginator(allplayers,100)
			page = request.GET.get('page')
			try:
				playerlist = players.page(page)
			except PageNotAnInteger:
				playerlist = players.page(1)
			except EmptyPage:
				playerlist = players.page(paginator.num_pages)
		finally:
			cursor.close()
	return render(request,
		'leaderboards/index.html',
		{'players':playerlist})


def indexdmrecent(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename, rating, player_id, steamid, active, lastplayed FROM dmplayer ORDER BY lastplayed DESC;")
			allplayers = cursor.fetchall()
			players = Paginator(allplayers,100)
			page = request.GET.get('page')
			try:
				playerlist = players.page(page)
			except PageNotAnInteger:
				playerlist = players.page(1)
			except EmptyPage:
				playerlist = players.page(paginator.num_pages)
		finally:
			cursor.close()
	return render(request,
		'leaderboards/index.html',
		{'players':playerlist})

def playerview(request, pk):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT killer_name,killer_id, victim_name,victim_id, dateoccurred, weapon, matchup_id FROM matchup WHERE killer_id = (%s) OR victim_id = (%s) ORDER BY dateoccurred DESC;",
				(pk, pk))
			matchuplist = cursor.fetchall()
			ratinghistory = playerrating(int(pk))
			playerdata = playername(pk)
		finally:
			cursor.close()
	return render(request, 
		'leaderboards/player.html',
		{'matchuplist':matchuplist,
		'ratinghistory': ratinghistory,
		'playername':playerdata.get('ingamename'),
		'playerrating':playerdata.get('rating'),
		'pk': int(pk)})

def playerdmview(request, pk):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT killer_name,killer_id, victim_name,victim_id, dateoccurred, weapon, matchup_id FROM dmmatchup WHERE killer_id = (%s) OR victim_id = (%s) ORDER BY dateoccurred DESC;",
				(pk, pk))
			matchuplist = cursor.fetchall()
			ratinghistory = playerratingdm(int(pk))
			playerdata = playernamedm(pk)
		finally:
			cursor.close()
	return render(request, 
		'leaderboards/playerdm.html',
		{'matchuplist':matchuplist,
		'ratinghistory': ratinghistory,
		'playername':playerdata.get('ingamename'),
		'playerrating':playerdata.get('rating'),
		'pk': int(pk)})

def playerratingdm(pk):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT killerrating, dateoccurred FROM dmmatchup WHERE killer_id = (%s) ORDER BY dateoccurred DESC",
				(pk,))
			ratingincreases = cursor.fetchall()
			cursor.execute("SELECT victimrating, dateoccurred FROM dmmatchup WHERE victim_id = (%s) ORDER BY dateoccurred DESC",
				(pk,))
			ratingdecreases = cursor.fetchall()
		finally:
			cursor.close()
			ratinglist = ratingincreases+ratingdecreases
			ratinglist.sort(key = lambda x: x[1])
			ratinglist = ratinglist[-100:]
			return map((lambda x: x[0]), ratinglist)

def playerrating(pk):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT killerrating, dateoccurred FROM matchup WHERE killer_id = (%s) ORDER BY dateoccurred DESC",
				(pk,))
			ratingincreases = cursor.fetchall()
			cursor.execute("SELECT victimrating, dateoccurred FROM matchup WHERE victim_id = (%s) ORDER BY dateoccurred DESC",
				(pk,))
			ratingdecreases = cursor.fetchall()
		finally:
			cursor.close()
			ratinglist = ratingincreases+ratingdecreases
			ratinglist.sort(key = lambda x: x[1])
			ratinglist = ratinglist[-100:]
			return map((lambda x: x[0]), ratinglist)

def playername(pk):
	with connection.cursor() as cursor:
		cursor.execute("SELECT ingamename,rating FROM player WHERE player_id = (%s);",
				(pk,))
		playerign = cursor.fetchone()
		if playerign is not None:
			return {'ingamename': playerign[0],
			'rating':playerign[1]}
	return playerign
def playernamedm(pk):
	with connection.cursor() as cursor:
		cursor.execute("SELECT ingamename,rating FROM dmplayer WHERE player_id = (%s);",
				(pk,))
		playerign = cursor.fetchone()
		if playerign is not None:
			return {'ingamename': playerign[0],
			'rating':playerign[1]}
def graph(request):
	with connection.cursor() as cursor:
		cursor.execute("SELECT rating FROM player ORDER BY rating ASC;")
		ratinglist = cursor.fetchall()
		ratinglist = map((lambda x: x[0]), ratinglist)
		indices = map((lambda x: str(x)), createrange(ratinglist,20))
		bins = createfrequency(ratinglist, 20)

		cursor.execute("SELECT weapon FROM matchup ORDER BY dateoccurred DESC LIMIT 1000;")
		weaponlist = cursor.fetchall()
		weaponlist = map((lambda x: x[0]), weaponlist)
		weaponcounts = Counter(weaponlist)
		weapons, frequency = weaponcounts.keys(), weaponcounts.values()
		weapons = map((lambda x: str(x)), weapons)
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

def searchplayer(request):
	if request.method == 'POST':
		search_term = request.POST.get('player_search')
		players = isearch(search_term)
		dmplayers = players.get('dmplayers')
		tdmplayers = players.get('players')
		return render(request,
			'leaderboards/searchresults.html',
			{'tdmplayers':tdmplayers,
			'dmplayers':dmplayers})

def isearch(search_term):
	with connection.cursor() as cursor:
		cursor.execute("""
			SELECT ingamename, rating, player_id FROM player
			WHERE ingamename ILIKE '%%' || %s || '%%'
			LIMIT 15""",
			(search_term,))
		players = cursor.fetchall()
		cursor.execute("""SELECT ingamename,rating, player_id FROM dmplayer
			WHERE ingamename ILIKE '%%' || %s || '%%'
			LIMIT 15""",
			(search_term,))
		dmplayers = cursor.fetchall()
	return {'players': players,
	'dmplayers' : dmplayers}