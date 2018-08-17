from django.db import models
from userinfo.models import UserInfo

# Create your models here.
class Movie(models.Model):
    title = models.CharField('片名', max_length=50, null=False)
    country = models.CharField('国家', max_length=100)
    date = models.CharField('时间', max_length=50)
    mtype = models.CharField('类型', max_length=50)
    language = models.CharField('语言', max_length=30)
    director = models.CharField('导演', max_length=200)
    actor = models.CharField('主演', max_length=500)
    scriptwriter = models.CharField('编剧', max_length=500)
    introduction = models.CharField('简介', max_length=1000)
    # picture = models.ImageField('海报', upload_to='static/images/movie', default='normal.jpg')
    picture = models.CharField('海报', max_length=200)

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return self.title

    def get_movie_url(self):
        return '/single/{}'.format(self.id)


class Comment(models.Model):
    content = models.CharField('评论', max_length=1000)
    com_time = models.DateTimeField('评论时间', auto_now=True)
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(UserInfo)

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.movie.title


class Grade(models.Model):
    star = models.DecimalField('评分', max_digits=2, decimal_places=1)
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(UserInfo)

    class Meta:
        db_table = 'grade'

    def __str__(self):
        return self.movie.title
