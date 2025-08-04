from django.contrib.auth import get_user_model

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .models import *
from .forms import *


# Create your views here.
def home(request):
	posts = []

	if request.method == 'GET':
		posts = Post.objects.all().order_by('-id')
	elif request.method == 'POST':
		posts = Post.objects.all().order_by('-id')
		data = request.POST.get('search-data')
		if data:
			posts = [x for x in posts if data.lower() in x.title.lower() or data == str(x.id) or data.lower() in str(x.category).lower()]

	return render(request, 'news/home.html', {
		'posts': posts
	})


def admin_panel(request):
	if request.user.is_authenticated:

		posts = []

		if request.method == 'GET':
			posts = Post.objects.all().order_by('-id')
		elif request.method == 'POST':
			posts = Post.objects.all().order_by('-id')
			data = request.POST.get('search-data')
			if data:
				posts = [x for x in posts if data.lower() in x.title.lower() or data == str(x.id) or data.lower() in str(x.category).lower()]

		return render(request, 'news/admin_panel.html', {
			'posts': posts
		})

	else:
		return HttpResponseRedirect('/login')


def ap_post_detail(request, pid):
	if request.user.is_authenticated:

		if request.method == 'GET':
			post = Post.objects.filter(id=pid)
			if post.exists():

				post = post[0]

				return render(request, 'news/post_detail.html', {
					'post': post
				})

			else:
				return HttpResponse(status=404)

		elif request.method == 'POST':
			pass

	else:
		return HttpResponse(status=404)


def load_file(request, pid):
	post = Post.objects.filter(id=pid)

	if post.exists():
		post = post[0]
		if post.file:
			return FileResponse(open(post.file.path, 'rb'))
		return HttpResponse(status=404)
	return HttpResponse(status=404)


def ap_post_edit(request, pid):
	if request.user.is_authenticated:

		if request.method == 'GET':
			post = Post.objects.filter(id=pid)
			if post.exists():
				post = post[0]

				form = EditPostForm(instance=post)

				return render(request, 'news/edit_post.html', {
					'post': post,
					'form': form
				})

			else:
				return HttpResponse(status=404)

		elif request.method == 'POST':

			post = Post.objects.filter(id=pid)
			if post.exists():
				post = post[0]
				form = EditPostForm(request.POST, request.FILES, instance=post)
				if form.is_valid():
					post = form.save()
					return HttpResponseRedirect(f'/admin_panel/post/{post.id}')
				else:
					return render(request, 'news/edit_post.html', {
						'post': post,
						'form': form
					})
			else:
				return HttpResponse(status=404)

	else:
		return HttpResponse(status=404)


def ap_post_delete(request, pid):
	if request.user.is_authenticated:

		if Post.objects.filter(id=pid).exists():
			Post.objects.filter(id=pid).delete()
			return HttpResponseRedirect('/admin_panel')
		else:
			return HttpResponse(status=404)

	else:
		return HttpResponse(status=404)


def add_post(request):
	if request.user.is_authenticated:

		if request.method == 'GET':
			form = EditPostForm()

			return render(request, 'news/add_post.html', {
				'form': form
			})

		elif request.method == 'POST':

			form = EditPostForm(request.POST, request.FILES)
			if form.is_valid():

				post = form.save(commit=False)
				post.author = f'{request.user.first_name} {request.user.last_name}'
				post.save()
				return HttpResponseRedirect(f'/admin_panel/post/{post.id}')
			else:
				return render(request, 'news/add_post.html', {
					'form': form
				})

	else:
		return HttpResponse(status=404)


def login_view(request):
	if request.method == 'GET':
		return render(request, 'news/login.html')
	elif request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		usr = authenticate(request, username=username, password=password)
		if usr is not None:
			user_login(request, usr)
			return HttpResponseRedirect('/admin_panel')
		else:
			return render(request, 'news/login.html')


def logout_view(request):
	user_logout(request)
	return HttpResponseRedirect('/')


def about(request):
	return render(request, 'news/about.html')
