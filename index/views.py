import logging
import random

from django.db import DatabaseError
from django.shortcuts import render, HttpResponse, redirect
from .models import Movie, Comment, Grade
from userinfo.models import *
import json


# Create your views here.
def index_views(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', locals())


def single_views(request, mid):
    user_id = request.session.get('user_id')
    if not user_id:
        username = 'Login'
    else:
        user = UserInfo.objects.filter(id=user_id)[0]
        username = user.uname
    movies = Movie.objects.filter(id=mid)
    if not movies:
        return redirect(request, 'index')
    movie = movies[0]

    comments = Comment.objects.filter(movie_id=mid).order_by('id').reverse()
    grade = Grade.objects.filter(movie_id=mid)[0].star

    movieAll = Movie.objects.all()
    movieList = [i for i in movieAll]
    items = random.sample(movieList, 4)
    return render(request, 'single.html', locals())


def comment_views(request, mid):
    content = request.POST.get('user_comment', 'normal')
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    dic = {
        'content': content,
        'movie_id': mid,
        'user_id': user_id,
    }
    obj = Comment(**dic)
    try:
        obj.save()
    except DatabaseError as e:
        logging.warning(e)
    return redirect('/single/{}'.format(mid))


def star_views(request, mid):
    grade = Grade()
    grade.star = int(request.POST.get('stars-rating', '0'))
    grade.user_id = request.session.get('user_id')
    grade.movie_id = mid
    try:
        grade.save()
    except DatabaseError as e:
        logging.warning(e)
    return HttpResponse('OK')


def addm_views(request):
    with open('/home/tarena/xiaoshu/Project/OrangeMovie/index/doubanhot.text', 'r') as fr:
        for fjson in fr:
            if fjson != '\n':
                item = json.loads(fjson)
                # print(item['title'])
                movie = Movie()
                movie.title = item['title']
                movie.country = item['country']
                movie.date = item['time']
                movie.actor = item['actor']
                movie.director = item['derector']
                movie.scriptwriter = item['scripts']
                movie.picture = item['pic']
                movie.introduction = item['intro']
                movie.language = item['lang']
                movie.mtype = item['type']
                movie.save()
    return HttpResponse('OK')


def addcom_views(request):
    with open('/home/tarena/xiaoshu/Project/OrangeMovie/index/doubanhot.text', 'r') as fr:
        for fjson in fr:
            if fjson == '\n':
                continue
            item = json.loads(fjson)
            mtitle = item['title']
            movie = Movie.objects.filter(title=mtitle)[0]
            print(movie.title, 'start')
            for content in item['comments']:
                comm = Comment()
                comm.content = content
                comm.movie = movie
                comm.user_id = 3
                comm.save()
            print(movie.title, 'OK')
    return HttpResponse('OK')


def addstar_views(request):
    with open('/home/tarena/xiaoshu/Project/OrangeMovie/index/doubanhot.text', 'r') as fr:
        for fjson in fr:
            if fjson == '\n':
                continue
            item = json.loads(fjson)
            star = item['grade']
            if not star:
                star = 0.0
            movie = Movie.objects.filter(title=item['title'])[0]
            grade = Grade()
            grade.star = float(star)
            grade.movie = movie
            grade.user_id = 3
            grade.save()
    return HttpResponse('OK')
