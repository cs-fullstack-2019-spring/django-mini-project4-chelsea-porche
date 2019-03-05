from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Game, Person
from .forms import NewUserForm, NewGameForm

# Create your views here.

# TO REQUIRE LOGIN TO VIEW PAGE
@login_required
def index(request):
    # TO LOGIN SPECIFIC USER
    userLogin = Person.objects.filter(userForeignKey=request.user)
    # TO GRAB GAME OBJECTS
    gamer = Game.objects.all()
    # TO SYNC VARIABLES WITH HTML PAGE FORMAT
    context = {
        'userLogin': userLogin,
        'gamer': gamer,
    }
    # TO ROUTE FUNCTION TO PAGE
    return render(request, 'gameApp/index.html', context)


def createuser(request):
    # TO USE INFORMATION ENTERED IN FORM/PULL INFO FROM FORM TO DISPLAY
    new_user = NewUserForm(request.POST or None)
    # TO SAVE IF INFO VALIDATES
    if new_user.is_valid():
        new_user.save()
        # TO RETURN TO INDEX AFTER SUBMIT
        return redirect('index')
    # FOR DISPLAYING FORM INFO ON HTML FROM FORM/MODEL
    context = {
        'userform': new_user
    }
    # TO ROUTE TO/FROM CREATE USER HTML
    return render(request, 'gameApp/createuser.html', context)


def creategame(request):
    # TO GRAB OBJECTS FROM GAME FORM/MODEL
    gameform = NewGameForm(request.POST or None)
    # TO SAVE IF INFO VALIDATES
    if gameform.is_valid():
        gameform.save()
        # TO RETURN TO INDEX AFTER SUBMIT
        return redirect('index')
        # FOR DISPLAYING FORM INFO ON HTML FROM FORM/MODEL
    context = {
        'gameform': gameform
    }
    # TO ROUTE TO/FROM CREATEGAME HTML
    return render(request, 'gameApp/creategame.html', context)



def editgame(request,id):
    # TO GRAB SPECIFIC GAMER/USER
    gamer = get_object_or_404(Game, pk=id)
    # TO GRAB SELECTED GAME AND SEND TO FORM
    game_account = NewGameForm(request.POST or None, instance=gamer)
    # TO SAVE CHANGES
    if game_account.is_valid():
        game_account.save()
        # SEND BACK TO INDEX
        return redirect('index')
    # ROUTE TO HTML PAGE
    return render(request, 'gameApp/creategame.html', {'gameform': game_account})


def deleteaccount(request, id):
    # TO GRAB SPECIFIC ACCOUNT
    games = get_object_or_404(Game, pk=id)
    # TO DELETE IF SUBMITED/SAVE DELETE
    if request.method == 'POST':
        games.delete()
        # RETURN TO INDEX
        return redirect('index')
    # ROUTE TO/FROM DELETE CONFIRMATION PAGE
    return render(request, 'gameApp/delete.html', {'selectedgame': games})