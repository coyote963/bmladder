from django.shortcuts import render
from django.db import connection
# Create your views here.
def index(request):
	with connection.cursor() as cursor:
		try:
			cursor.execute("SELECT ingamename FROM player ORDER BY rating DESC;")
			playerlist = cursor.fetchall()
			playerlist = map(lambda x: x[0], playerlist)
		finally:
			cursor.close()
	return render(request,
		'leaderboards/index.html',
		{'playerlist':playerlist})
