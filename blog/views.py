from django.shortcuts import render
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('blog.can_add_post',raise_exception=True)
def post_new(request):
	if request.user.is_authenticated():
		form = PostForm()
		if request.method == "POST":
			form = PostForm(request.POST)
			if form.is_valid():
				post = form.save(commit=False)
				post.author = request.user
				post.date = timezone.now()
				post.save()
				return redirect('post_detail',pk=post.pk)
		return render(request, 'blog/post_edit.html',{'form':form})
