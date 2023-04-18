from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import First,Second,Third,Fourth,Fifth,Sixth,Seventh,Eighth,Odai,Content,Follow,Good,Goodgame
from .forms import OdaiForm,ContentForm,LoginForm,SignupForm,UserForm,FindUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

def index(request):
    return render(request,'book/index.html')

def osaindex(request):
    return render(request,'book/osaindex.html')

def first(request):
    data = First.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/First.html',pa)

def second(request):
    data = Second.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/Second.html',pa)

def third(request):
    data = Third.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/third.html',pa)

def ee(request):
    data = Fourth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/ee.html',pa)

def eein(request):
    return render(request,'book/eein.html')

def eenext(request):
    data = Fifth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/eenext.html',pa)

def eeenext(request):
    data = Sixth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/eeenext.html',pa)

def osake(request):
    data = Seventh.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/osake.html',pa)

def osakein(request):
    pa = {
        'osake' :'説明' ,
    }
    return render(request,'book/osakein.html',pa)

def osaket(request):
    data = Eighth.objects.all().order_by("?")[:1]

    pa = {
        'data' : data,
    }
    return render(request,'book/osaket.html',pa)

#create_account
def signup_view(request):
    if request.method == 'POST':

        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/book/login')

    else:
        form = SignupForm()
    
    param = {
        'form': form
    }

    return render(request, 'book/signup.html', param)

#login_view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            if user:
                login(request, user)
                return redirect(to='/book/user')

    else:
        form = LoginForm()

    param = {
        'form': form,
    }

    return render(request, 'book/login.html', param)

#after login
@login_required(login_url='/admin/login/')
def user(request):
    datas = Follow.objects.filter(user=request.user).values_list('follow')
    data = Odai.objects.filter(user__in=datas).order_by('id').reverse()

    pa = {
        'data':data
    }

    return render(request,'book/user.html',pa)

#newgame create
@login_required(login_url='/admin/login/')
def new(request):
    data = Odai.objects.filter(user=request.user).count()
    if (request.method == 'POST'):
        od = Odai()
        form = OdaiForm(request.POST,instance=od)
        odai = form.save(commit=False)
        odai.user = request.user
        if data > 1 :
            messages.info(request,"二個以上は登録ができません")
            return redirect('new')
        
        else:
            odai.save()
            return redirect('choice')

    pa = {
        'form' : OdaiForm(), 
        'data' :data,
    }
    return render(request,'book/new.html',pa)

#after newgame choice gameview
@login_required(login_url='/admin/login/')
def choice(request):
    data = Odai.objects.filter(user=request.user).last()

    pa = {
        'data' : data
    }

    return render(request,'book/choice.html',pa)

#after choice gameview content enter
@login_required(login_url='/admin/login/')
def content(request,num):
    post = Odai.objects.get(id=num)
    data = Odai.objects.all().get(id=num)
    datas = Content.objects.filter(userid=request.user,title=data)
    yay = Content.objects.filter(title=data).count()

    if request.method == 'POST':
        #ゲーム内容入力フォーム
        if request.POST['mode'] == '_contentform_':
            co = Content()
            form = ContentForm(request.POST,instance=co)
            co = form.save(commit=False)
            co.userid = request.user
            co.title = post
            if yay > 19:
                messages.info(request,"19個以上は登録ができません")
                return redirect('content',num=num)
            else:
                co.save()
                return redirect('content',num=num)

    if request.method == 'POST':
        if request.POST['mode'] == '_deleteform_':
            datass.delete()
            return redirect('content',num=num)

    pa = {
        'form':ContentForm(instance=post),
        'data':data,
        'datas':datas,
        'id':num,
        'yay':yay
    }

    return render(request,'book/content.html',pa)

#投稿済みゲーム確認
@login_required(login_url='/admin/login/')
def post(request):
    data = Odai.objects.filter(user=request.user)

    pa = {
        'data':data
    }

    return render(request,'book/post.html',pa)

#
@login_required(login_url='/admin/login/')
def start(request,num):
    fu = Odai.objects.get(id=num)
    data = Content.objects.filter(userid=request.user,title=fu).order_by("?")[:1]

    pa = {
        'data':data
    }

    return render(request,'book/start.html',pa)


@login_required(login_url='/admin/login/')
def startt(request,num):
    fu = Odai.objects.all().get(id=num)
    datas = Follow.objects.filter(user=request.user).values_list('follow')
    data = Content.objects.filter(title=fu)
    lolo = Odai.objects.filter(id=num)

    pa = {
        'data':data,
        'lolo':lolo,
        'fu':fu
    }

    return render(request,'book/startt.html',pa)


@login_required(login_url='/admin/login/')
def starttt(request,num):
    fu = Odai.objects.get(id=num)
    data = Content.objects.filter(title=fu).order_by("?")[:1]

    pa = {
        'data':data
    }

    return render(request,'book/starttt.html',pa)

#ゲームを消去する画面
@login_required(login_url='/admin/login/')
def delete(request,num):
    data = Odai.objects.get(id=num)
    if (request.method == 'POST'):
        data.delete()
        return redirect('user')

    pa = {
        'data':data,
        'id':num #必要
    }
    return render(request,'book/delete.html',pa)


@login_required(login_url='/admin/login/')
def favorite(request):
    #いいねしたゲームを取得
    data = Good.objects.filter(user=request.user)

    pa = {
        'data':data,
    }
    return render(request,'book/follow.html',pa)


@login_required(login_url='/admin/login/')
def whogood(request):
    datas = Follow.objects.filter(user=request.user).values_list('follow')
    #？？_in=リストで「ある形がリストに含まれているか検索を行える．」
    data = Goodgame.objects.filter(user__in=datas)

    if request.method =='POST':
        if request.POST['mode'] == '_userform_':
             #から探せる探索フォーム
             userform = UserForm(request.POST)
             str = request.POST['user']
             data = Goodgame.objects.filter(user__username__contains=str).order_by('id').reverse()#ユーザが入力された文字を含むレコードを抽出

    else:
        #通常の画面
        userform = UserForm()
        data
        #コメントが寄せられたもの全て表示される．同じアニメが何件も表示される．

    pa = {
        'data':data,
        'userform':userform,
    }

    return render(request,'book/whogood.html',pa)


@login_required(login_url='/admin/login/')
def mypage(request):
    datas = Follow.objects.filter(user=request.user)

    pa = {
        'datas':datas,
    }
    return render(request,'book/mypage.html',pa)


@login_required(login_url='/admin/login/')
def mypage2(request):

    if request.method =='POST':
        if request.POST['mode'] == '_userform_':
             #から探せる探索フォーム
             userform = UserForm(request.POST)
             str = request.POST['user']
             data = User.objects.filter(username__contains=str).order_by('id').reverse()#ユーザが入力された文字を含むレコードを抽出

    else:
        #通常の画面
        userform = UserForm()
        data = User.objects.all().order_by('id').reverse()

    pa = {
        'data':data,
        'userform':userform
    }
    return render(request,'book/mypage2.html',pa)


@login_required(login_url='/admin/login/')
def deleteuser(request,num):
    data = Follow.objects.get(id=num)
    if (request.method == 'POST'):
        data.delete()
        return redirect('mypage')

    pa = {
        'data':data,
        'id':num #必要
    }
    return render(request,'book/deleteuser.html',pa)

@login_required(login_url='/admin/login/')
def deletecontent(request,num):
    data = Content.objects.get(id=num)
    tiu = Content.objects.values_list('title',flat=True).get(id=num)#お題を取り出す
    hito = Odai.objects.filter(id=tiu).values_list('id',flat=True)
    datas = Odai.objects.get(id=tiu)#お題のIDを取り出す必要がある
    if (request.method == 'POST'):
        data.delete()
        return redirect('content',num=tiu)

    pa = {
        'data':data,
        'id':num #必要
    }
    return render(request,'book/deletecontent.html',pa)

@login_required(login_url='/admin/login/')
def followOdai(request,num):
    data = Follow.objects.values_list('follow').get(id=num)#id取得してる
    datas = Odai.objects.filter(user=data)
    asia = Follow.objects.filter(user=request.user,follow__username=data)
    asiao = Follow.objects.filter(user__username=data)


    pa = {
        'datas':datas,
        'asia':asia,
        'id':num #必要
    }
    

    return render(request,'book/followOdai.html',pa)


@login_required(login_url='/admin/login/')
def add(request):
    #追加するUserを取得
    add_name = request.GET['name']
    add_user = User.objects.filter(username=add_name).first()
    #Userが本人だった場合
    if add_user == request.user:
        messages.info(request,"自分自身を追加することはできません")
        return redirect('mypage2')

    
    #add_userの数を調査
    frd_num = Follow.objects.filter(user=request.user).filter(follow=add_user).count()

    (public_user) = get_public()

    #ゼロより大きければ既に登録してある．
    if frd_num > 0 :
        messages.info(request,add_user.username + 'は既に追加されています')
        return redirect('mypage2')

    frd = Follow()
    frd.user = request.user
    frd.follow = add_user
    frd.save()
    #保存された時のメッセージを設定
    messages.success(request,add_user.username + 'を追加しました')
    return redirect('mypage2')

#フォロー欄とゲーム欄で分別する

def get_public():
    public_user = User.objects.filter(username='public').first()
    return (public_user)


@login_required(login_url='/admin/login/')
def god(request,odai_id):
    #いいねするゲームを取得
    god_msg = Odai.objects.get(id=odai_id)
    #自分がゲームにGoodした数を調べる
    is_good = Goodgame.objects.filter(user=request.user).filter(good=god_msg).count()
    #ゼロより大きければ登録済み
    if is_good > 0:
        messages.success(request,"過去にいいねをしています")
        return redirect('startt',num=odai_id)
    
    god_msg.save()
    god = Goodgame()
    god.user = request.user
    god.good = god_msg
    god.save()
    messages.success(request,"いいねしました")
    return redirect('startt',num=odai_id)

