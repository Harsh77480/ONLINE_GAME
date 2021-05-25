from django.shortcuts import render
from .models import Game,Player
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def createRoom(request):
    game = Game.objects.create()
    p = Player.objects.create(game = game)
    return redirect('gameWaiting' , p_name = p.p_code )

def joinRoom(request,code):
    print(code)
    try :
        game = get_object_or_404(Game,game_code = code)
        ps = Player.objects.filter(game = game)
        print(len(ps))
        if(len(ps)<2):
            p = Player.objects.create(game = game) 
        else:
            return render(request, 'error.html', {}) # room full
    except :
        return render(request, 'error.html', {}) # room not exists
    return redirect('gameWaiting' , p_name = p.p_code )



def gameWaiting(request,p_name):
    p = get_object_or_404(Player,p_code = p_name)
    game = p.game
    return render(request, 'game_waiting.html', {'room_name': game.game_code , 'p_name' : p_name })

def gameOn(request,p_name,room_name):
    p = get_object_or_404(Player,p_code = p_name)
    game = p.game
    return render(request, 'game_on.html', {'room_name': game.game_code , 'p_name' : p_name })


def endGame(request, p_name):
    x = "false"
    p = get_object_or_404(Player,p_code = p_name)
    game = p.game
    if(game.p == p_name or game.p == ''):
        x = "true"
    
    p.delete()#deleting the player

    p = Player.objects.filter(game = game)
    if( not p.exists() ):
        game.delete()#delete game if noone exists

    return render(request , 'endGame.html' , {'uWon' : x} )

def Error(request):
    return render(request , 'error.html' , {} )
    