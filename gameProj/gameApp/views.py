from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Game, Person
from .forms import NewUserForm, NewGameForm

# Create your views here.
@login_required
def index(request):
    userLogin = Person.objects.filter(userForeignKey=request.user)
    gamer = Game.objects.all()
    context ={
        'userLogin': userLogin,
        'gamer': gamer,
    }
    return render(request, 'gameApp/index.html', context)


def createuser(request):
    new_user = NewUserForm(request.POST or None)
    if new_user.is_valid():
        new_user.save()
        return redirect('index')
    context = {
        'userform': new_user
    }
    return render(request, 'gameApp/createuser.html', context)


def creategame(request):
    gameform = NewGameForm(request.POST or None)
    if gameform.is_valid():
        gameform.save()
        return redirect('index')
    context = {
        'gameform': gameform
    }
    return render(request, 'gameApp/creategame.html', context)



def editgame(request,id):
    gamer = get_object_or_404(Game, pk=id)
    game_account = NewGameForm(request.POST or None, instance=gamer)
    if game_account.is_valid():
        game_account.save()
        return redirect('index')
    return render(request, 'gameApp/creategame.html', {'gameform': game_account})


def deleteaccount(request, id):
    games = get_object_or_404(Game, pk=id)
    print(request.POST)
    if request.method == 'POST':
        games.delete()
        return redirect('index')
    return render(request, 'gameApp/delete.html', {'selectedgame': games})