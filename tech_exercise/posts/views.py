from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Article
from .forms import PostForm
import datetime

# Create your views here.

def index(request):
	latest_article = Article.objects.order_by('-pub_date')[0]
	latest_article_list = Article.objects.order_by('-pub_date')[1:]
	context = {'latest_article': latest_article,'latest_article_list': latest_article_list,
	}
	#return HttpResponse("output")
	return render(request, 'posts/index.html', context)

def article(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Question.DoesNotExist:
		raise Http404("Article does not exist")
	return render(request, 'posts/article.html', {'article': article})

	

def article_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.pub_date = datetime.datetime.now()
			post.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request, 'posts/article_edit.html', {'form': form})

	