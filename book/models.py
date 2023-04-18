from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.



class First(models.Model):
    content  = models.TextField(max_length=100000)


class Second(models.Model):
    Scontent = models.TextField(max_length=100000)

class Third(models.Model):
    Tcontent = models.TextField(max_length=100000)

class Fifth(models.Model):
    Fcontent = models.TextField(max_length=10000000)

class Sixth(models.Model):
    Scontent = models.TextField(max_length=10000000)

class Seventh(models.Model):
    Secontent = models.TextField(max_length=10000000)

class Eighth(models.Model):
    Econtent = models.TextField(max_length=10000000)

class Fourth(models.Model):
    Fcontent = models.TextField(max_length=10000000)

class Title(models.Model):
    title = models.CharField(max_length=2000)

class Rule(models.Model):
    rule = models.TextField(max_length=100000000000)

class Inside(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='ユーザ')
    title = models.ForeignKey(Title,on_delete=models.CASCADE,verbose_name='タイトル')
    content = models.TextField(max_length=100000000000000000)

class Odai(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='ユーザ')
    odai = models.TextField(max_length=1000000000000)

class Content(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='ユーザ')
    title = models.ForeignKey(Odai,on_delete=models.CASCADE,verbose_name='タイトル')
    content = models.TextField(max_length=100000000000000000)

class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='ユーザ',related_name="userowner")
    follow = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='フォロー')

class Good(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='ユーザ')
    good = models.ForeignKey(Content,on_delete=models.CASCADE,verbose_name='いいね')

class Goodgame(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='ユーザ')
    good = models.ForeignKey(Odai,on_delete=models.CASCADE,verbose_name='いいね')


