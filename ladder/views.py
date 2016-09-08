from django.shortcuts import render, render_to_response
from ladder.forms import TournamentForm, CommentForm
from django.template import RequestContext
from ladder.models import Tournament,Participant,Match
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from datetime import datetime
from django.shortcuts import redirect, get_object_or_404
from player.models import Profile
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin

class index(ListView):
	model = Tournament
	template_name = 'ladder/index.html'
def matchhistory(request, pk):
	tournament = get_object_or_404(Tournament, pk = pk)
	return render(request,
		'ladder/matchhistory.html',
		{'matchlist': tournament.match_set.all()})
class detail(DetailView):

	def post(self, request, *args, **kwargs):
		object = super(detail, self).get_object()
		new_participant = Participant(user = request.user,latest_activity = datetime.now(), ranking = object.participants.count()+1)
		new_participant.save()
		object.participants.add(new_participant)
		return redirect('detail', object.pk)

	model = Tournament
	template_name = 'ladder/tournamentpage.html'
	def get_context_data(self, **kwargs):
		context = super(detail, self).get_context_data(**kwargs)
		object = super(detail, self).get_object()
		rankinglist = object.participants.all().order_by('ranking')
		context['players_ranked'] = rankinglist
		try:
			if object.participants.all().filter(user = self.request.user).exists():
				context['in_tournament'] = True
			else:
				context['in_tournament'] = False
		except:
			context['in_tournament']= False
		context['self.request'] = self.request
		return context

# Create your views here.
@login_required
@permission_required('ladder.can_add_tournament',raise_exception=True)
def createtournament(request):
	context = RequestContext(request)
	if request.method == 'POST':
		print 'POST'
		tournament_form = TournamentForm(data=request.POST)
		if tournament_form.is_valid():
			tournament = tournament_form.save()
			tournament.save()
			return redirect('ladderindex')
		else:
			print tournament_form.errors
	else:
		tournament_form = TournamentForm()
	return render(request,
		'ladder/createtournament.html',
		{'tournament_form':tournament_form},
		)
@login_required
def add_comment_to_post(request, pk):
    tournament = get_object_or_404(Tournament, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.tournament = tournament
            new_comment.save()
            return redirect('detail', pk)
    else:
        form = CommentForm()
    return render(request, 
    	'ladder/add_comment_to_post.html',
    	{'form': form},
    	)
@login_required
@permission_required('ladder.can_change_tournament',raise_exception=True)
def reportmatch(request, pk):
	tournament = get_object_or_404(Tournament, pk = pk)
	try:
		player1 = tournament.participants.get(pk=request.POST['player1'])
		player2 = tournament.participants.get(pk = request.POST['player2'])

		score1 = request.POST['score1']
		score2 = request.POST['score2']
	except (KeyError, Participant.DoesNotExist):

		return render(request,'ladder/reportmatch.html', {
			'tournament' : tournament,
			'error_message':"Pick two players",
		})
	else:
		player1.latest_activity = datetime.now()
		player2.latest_activity = datetime.now()
		if player1.ranking > player2.ranking: #player1 is lower ranked player
			if score1 >= score2: #upset occured
				player2.latest_loss = datetime.now()
				switch(player1,player2)
				match = Match(tournament = tournament,
					date = datetime.now(), 
					winner = player1, loser = player2,
					score_winner = score1, score_loser = score2)
				match.save()
				match.winner.add(player1)
				match.loser.add(player2)
			else:
				player1.latest_loss = datetime.now()
				match = Match(tournament = tournament, 
					date = datetime.now(), 
					winner = player2, loser = player1,
					score_winner = score2, score_loser = score1)
				match.save()
				match.winner.add(player2)
				match.loser.add(player1)

		else: #player1 is better ranked than player2
			if score2 > score1:
				player1.latest_loss = datetime.now()
				switch(player1 = player1, player2 = player2)
				match= Match(score_loser = score1, score_winner = score2, 
					winner = player2, loser = player1, 
					tournament = tournament)
				match.save()
	
			else:#score1 > score2
				player2.latest_loss = datetime.now()
				match = Match(tournament = tournament,
					date = datetime.now(), 
					score_winner = score1, score_loser = score2,
					winner = player1, loser = player2)
				match.save()
		match.save()
		return redirect('detail', pk)
def switch(player1, player2):
	temp = player2.ranking
	player2.ranking = player1.ranking
	player1.ranking = -1
	player1.save()
	player2.save()
	player1.ranking = temp
	player1.save()

